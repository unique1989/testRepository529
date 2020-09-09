import requests


headers = {"Content-Type": "application/json"}
payload = {'key1': 'hello', 'key2': 'world'}
files = {'file': open('interface_url.xlsx', 'rb')}

# r = requests.post('http://httpbin.org/post', data=payload, headers=headers)
r = requests.post('http://httpbin.org/post', files=files)

print(r.url)
print(r.text)
print(r.status_code)