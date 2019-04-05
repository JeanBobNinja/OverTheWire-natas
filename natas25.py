#
import requests

username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

url = "http://%s.natas.labs.overthewire.org" % username

r = requests.post(url, auth=(username,password))
print(r.text)