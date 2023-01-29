import requests
import sys
import pprint
import json

headers = {
    'accept': 'application/json',
}

data = {
    'grant_type': '',
    'username': 'kate142',
    'password': '123456',
    'scope': '',
    'client_id': '',
    'client_secret': '',
}

response = requests.post('http://localhost:8080/v1/login', headers=headers, data=data)

assert response.status_code == 200
pprint.pprint(
    json.loads(response.content.decode()))