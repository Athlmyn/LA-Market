import requests

url = "https://www.lostarkmarket.online/api/export-market-live/North America East/?ids=101301,101011"
#"region" : "North America East"
payload={   
            "items": "basic-oreha-fusion-material-2" }
headers = {}


response = requests.request("GET", url, headers=headers, data=payload)

variable = "Marisol Quintero"

print(response.text)