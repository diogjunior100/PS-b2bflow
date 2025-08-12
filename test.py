import requests
import json

url = "https://api.z-api.io/instances/3E59DC356725101DEC67DEA70E730544/token/5529D9572FA545730C243FBF/send-text"

payload = {
    "phone": "5586999108399",
    "message": "Olá, esta é uma mensagem de teste!"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())