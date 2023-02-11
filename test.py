import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "shorten/www.oracle.com/myname")

print(response.json())