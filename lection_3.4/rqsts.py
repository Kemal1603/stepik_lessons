import requests

res = requests.get('https://www.python.org')
print(res.status_code)
print(res.headers['Content-type'])
print(res.url)
with open('/home/kemal/Downloads/htmlfile.txt', 'w+') as f:
    f.write(res.text)
