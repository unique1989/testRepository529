import requests

payload = {'key1': 'hello', 'key2': 'world'}
r = requests.get('http://httpbin.org/get', params=payload)

print(r.url)
print(r.text)
print(r.status_code)