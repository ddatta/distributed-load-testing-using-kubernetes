import requests

url = "https://pkc-z1o60.europe-west1.gcp.confluent.cloud:443/kafka/v3/clusters/lkc-6w31m8/topics/iotdemotopic/records"
data = '{"value":{"type":"JSON","data":"Hello World!"}}'
headers = {'Content-type': 'application/json',
               'Authorization': 'Basic UzNYNzJWWVFDVVo1NFlLUzpiT0Q2c1FuVHlLTWI4ZDd1RWJSVUNDQzdTdStQcG9LUUhqUThvMStheGw2RUQvNlRqTGlwMU84Y01aVVNteDB5'}

r = requests.post(url, data=data, headers=headers)
print(r.text)
