import requests

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))
print(r.text)