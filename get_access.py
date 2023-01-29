import requests
import sys
import pprint
import json


user_access_token = "eyJhbGciOiJIUzI1NiIsImV4cGlyZXNJbiI6IjMwbSIsImtpZCI6InNpbTIiLCJ0eXAiOiJKV1QifQ.eyJlbWFpbCI6ImthdGUxNDIiLCJleHAiOjE2NzUwMTczMjJ9.zfTSDi9asF7ujrb-Z_t_d7MMPT1xoy7S8ItfRnDvCVs"

res = requests.get('http://localhost:8080/v1/users', headers={'Authorization': f'Bearer {user_access_token}'})

assert res.status_code == 200
pprint.pprint(
    json.loads(res.content.decode())
)