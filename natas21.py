import requests

username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url = "http://%s.natas.labs.overthewire.org" % username

r = requests.get(url, auth=(username,password))
print(r.text)