import requests

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = "http://%s.natas.labs.overthewire.org" % username
r = requests.get(url, auth = (username,password))
print(r.text)