import requests

url = "http://python.furkanyolal.com.tr/denemeler/index.json"

response = requests.get(url)

json_verisi = response.json()

bool = (json_verisi["rates"])
print(bool)
