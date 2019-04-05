import requests

username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url = "http://%s.natas.labs.overthewire.org" % username

r = requests.get(url, auth=(username,password))
print(r.text)