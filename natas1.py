import requests

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

url = "http://natas1.natas.labs.overthewire.org"
session = requests.Session()
response = session.get(url, auth = (username,password))


print response.text