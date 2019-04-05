import requests

username = 'natas26'
password = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

url = "http://%s.natas.labs.overthewire.org" % username

r = requests.get(url, auth=(username,password))
print(r.text)