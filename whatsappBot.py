import requests

url = ' https://eu125.chat-api.com/instance155253/'
data = ({"phone": "9895437938"}, {"body": "Hello"})
res = requests.post(url, json=data)
print (res.text)