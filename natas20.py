import requests

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = "http://%s.natas.labs.overthewire.org" % username
r = requests.get(url, auth = (username,password))
print(r.text)