import requests

data = requests.get('https://protech-api.herokuapp.com/list')
print (data.text)