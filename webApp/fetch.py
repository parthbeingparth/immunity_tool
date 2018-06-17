import requests
import json

temp = requests.get('https://protech-api.herokuapp.com/list')
data = json.loads(temp.text)
print (data["data"][0])