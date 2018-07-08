import requests

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

response = session.get(url, auth = (username,password))

print response.text