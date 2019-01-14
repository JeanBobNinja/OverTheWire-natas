import requests

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))
print(r.text)