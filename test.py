import requests
import pprint

url = "http://localhost:8080/auth/realms/master/protocol/openid-connect/token"

payload = 'username=admin&password=admin&client_id=admin-cli&grant_type=password'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)
token = response.json()['access_token']


headers ={
    f'accept': 'application/json',
    f'Authorization': f'Bearer {token}'
}

url = "http://localhost:8080/auth/admin/realms/test/users"
response = requests.get(url, headers=headers)
pprint.pprint(response.json())

url = "http://localhost:8080/auth/admin/realms/test/groups"
response = requests.get(url, headers=headers)
pprint.pprint(response.json())
group_id = response.json()[0]['id']

url = f"http://localhost:8080/auth/admin/realms/test/groups/{group_id}"
response = requests.get(url, headers=headers)
pprint.pprint(response.json())

url = f"http://localhost:8080/auth/admin/realms/test/groups/{group_id}/members"
response = requests.get(url, headers=headers)
pprint.pprint(response.json())
