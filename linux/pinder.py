import requests
url_teamplate="https://simurg.space/gen_file?data=obs&date={date}"
date="2026-02-19"
url=url_teamplate.format(date=date)

response=requests.get(url=url,stream=True)
print(f"for {date} got: {response}")