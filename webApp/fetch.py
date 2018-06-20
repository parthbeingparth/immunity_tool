import requests
import json
from flask_table import Table, Col

items = list()
temp = requests.get('https://protech-api.herokuapp.com/list')
data = json.loads(temp.text)
for i in range(len((data["data"][0]["list"]))):
    items.append(list((data["data"][0]["list"][i]).values()))

print (items)


