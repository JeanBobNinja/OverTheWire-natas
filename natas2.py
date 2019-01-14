import requests

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url = "http://natas2.natas.labs.overthewire.org/files/users.txt"
session = requests.Session()
response = session.post(url, auth = (username,password))


print(response.text)