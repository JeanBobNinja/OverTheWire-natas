import requests

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))
print(r.text)