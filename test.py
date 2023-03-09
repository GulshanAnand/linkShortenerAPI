import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "shorten")

# print(response.content)

form_data = {'url': 'https://www.bing.com', 'alias' : 'coke'}

headers = {'Content-Type': 'application/json'}

server = requests.post(BASE + "shorten", data=form_data)
output = server.text

print(output)