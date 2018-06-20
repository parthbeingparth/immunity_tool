import requests
import json
from flask_table import Table, Col

items = list()
temp = requests.get('https://protech-api.herokuapp.com/list')
data = json.loads(temp.text)




class ItemTable(Table):
    name = Col('Name')
    version = Col('Version')
    date = Col('Date')
    vendor = Col('Vendor')
    status = Col("Status")

# Get some objects
class Item(object):
    def __init__(self, name, version, date, vendor, status):
        self.name = name
        self.version = version
        self.date = date
        self.vendor = vendor
        self.status = status
for i in range(len((data["data"][0]["list"]))):
    temp=list((data["data"][0]["list"][i]).values())
    items.append(Item(temp[0],temp[1],temp[2],temp[3],"Approved"))

table = ItemTable(items)

print(table.__html__())
