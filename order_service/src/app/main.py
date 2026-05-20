import os

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Order Service")

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:8001",
)
DISCOUNT_SERVICE_URL = os.getenv(
    "DISCOUNT_SERVICE_URL",
    "http://127.0.0.1:8003",
)


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promo_code: Optional[str] = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    subtotal: float
    discount_percent: float
    discount_amount: float
    total: float


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


class DiscountFromService(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    # 1. Получаем товар из product-service
    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )

    # 2. Получаем скидку из discount-service
    discount = await fetch_discount(
        product_id=order.product_id,
        quantity=order.quantity,
        unit_price=product.price,
        promo_code=order.promo_code,
    )

    # 3. Считаем итог
    subtotal = product.price * order.quantity
    discount_amount = subtotal * (discount.discount_percent / 100)
    total = subtotal - discount_amount

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        subtotal=subtotal,
        discount_percent=discount.discount_percent,
        discount_amount=discount_amount,
        total=total,
    )


async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())


async def fetch_discount(
    product_id: str,
    quantity: int,
    unit_price: float,
    promo_code: Optional[str] = None,
) -> DiscountFromService:
    url = f"{DISCOUNT_SERVICE_URL}/discounts/calculate"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(
                url,
                json={
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "promo_code": promo_code,
                },
            )

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Discount service is unavailable: {exc}",
        ) from exc

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Discount service returned an unexpected error",
        )

    return DiscountFromService.model_validate(response.json())