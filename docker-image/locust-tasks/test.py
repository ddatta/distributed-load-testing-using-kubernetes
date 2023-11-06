import requests
import uuid

url = "http://34.140.142.132/api/measurement"

id = str(uuid.uuid4())
data = '{"vehicleId":"'+id+'"}'
headers = {'Content-type': 'application/json'}
print(data)
r = requests.post(url, data=data, headers=headers)
print(r.text)
