import requests

BASE = "https://labwired.tech/"

# response = requests.get(BASE + "shorten")

# print(response.content)

json_data = {'url': 'https://www.python.org', 'alias' : 'python'}

headers = {'Content-Type': 'application/json'}

server = requests.post(BASE + "shorten", json=json_data, headers=headers)
output = server.text

print(output)
