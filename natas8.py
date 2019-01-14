import requests

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

response = session.post(url, auth = (username,password), data = {'secret' : 'oubWYf2kBq', 'submit' : 1})


print(response.text)