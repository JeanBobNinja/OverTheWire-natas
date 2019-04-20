import requests

username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

url = "http://%s.natas.labs.overthewire.org" % username

r = requests.get(url, auth=(username,password))
print(r.text)