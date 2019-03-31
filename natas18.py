import requests
import string
import re
import time

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))
print(r.text)