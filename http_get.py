import requests
api_url = "https://api.ipify.org"

result = requests.get(api_url)

xnj = result.text

print(xnj)