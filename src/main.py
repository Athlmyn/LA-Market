import requests

API = "https://www.lostarkmarket.online/api/export-market-live/:region?ids=101301,101011"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

variable = "Marisol Quintero"

print(response.text)