import requests

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

response = session.post(url, auth = (username,password), data = {'secret' : 'FOEIUWGHFEEUHOFUOIU', 'submit' : '1'})


print(response.headers,response.text)