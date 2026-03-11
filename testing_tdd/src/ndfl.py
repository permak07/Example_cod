def calculate_ndfl_lax(param):
    tier=[
        (0.0,0.0,0.13),
        (2_400_000.0,312_000.0, 0.15),
        (5_000_000.0,762_000.0,0.18),
          ]
    for start,addition, rate in tier:
        if param>start:
            return addition+(param-start)*rate
    return