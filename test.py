import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "shorten/www.oracle123.com")

print(response.json())