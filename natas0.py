import requests

username = "natas0"
password = "natas0"

url = "http://natas0.natas.labs.overthewire.org"
session = requests.Session()
response = session.post(url, auth = (username,password))


print response.text