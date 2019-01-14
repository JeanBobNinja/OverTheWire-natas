import requests

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

url = "http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
session = requests.Session()
response = session.get(url, auth = (username,password))


print(response.text)