import requests

username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = "http://%s.natas.labs.overthewire.org" % username

r = requests.post(url, auth=(username,password))
print(r.text)