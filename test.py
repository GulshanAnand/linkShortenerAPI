import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "shorten")

# print(response.content)

json_data = {'url': 'https://www.python.org', 'alias' : 'coke'}

headers = {'Content-Type': 'application/json'}

server = requests.post(BASE + "shorten", json=json_data, headers=headers)
output = server.text

print(output)