import requests

username = 'catleer'
url = 'https://api.github.com'
path = '/users/' + username

r = requests.get(url+path, stream=True)
print(r.url)
print(r.status_code)
print(r.encoding)
print("响应内容：", r.text)
print("-" * 50)
print("二进制响应内容：", r.content)
print("-" * 50)
print("json格式的响应内容：", r.json())
print("-" * 50)
print("原始响应内容：", r.raw)
print("-" * 50)
print(r.raw.read(100))
print("-" * 50)
with open("11.txt", 'wb') as fd:
    c = 1
    for chunk in r.iter_content(100):
        fd.write(chunk)
        c = c + 1
    print(c)





