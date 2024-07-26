
# Penetration Test Report

## Initial Port Scan

First, I used nmap to enumerate the ports:

```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

I checked port 80, which was hosting an HTML website. Note that it has a domain board.htb on the email website.

Then I included that in my /etc/hosts:

```
10.10.11.11    board.htb
```

## Website Analysis

After analyzing the entire website and finding nothing, I tried DNS enumeration with ffuf:

```
ffuf -u http://10.10.11.11 -H "Host: FUZZ.boardlight.htb" -fw 6243 -w ../wordists/subdomains-top1million-20000.txt 
```

The result:

```
crm                     [Status: 200, Size: 6360, Words: 397, Lines: 150]
```

So, I added this new domain to my hosts file too:

```
10.10.11.11    crm.board.htb
```

## CRM Application

Accessing this domain, I found a CRM with Dolibarr application. After searching about Dolibarr vulnerabilities, I found that there are vulnerabilities for Dolibarr but only when logged in.

So, I tried some default passwords:

```
login: admin
password: admin
```

Obvious :) When logged in, we can use CVE-2023-30253 to get a shell on the website.

## Exploring the Server

After logging in, I found the /home/larissa folder (probably user.txt is there). I walked through the folders in /var/www and found the MySQL config for Dolibarr:

```
/var/www/html/crm.board.htb/htdocs/conf/conf.php  
$dolibarr_main_db_host='localhost';
$dolibarr_main_db_port='3306';
$dolibarr_main_db_name='dolibarr';
$dolibarr_main_db_prefix='llx_';
$dolibarr_main_db_user='dolibarrowner';
$dolibarr_main_db_pass='serverfun2$2023!!';
$dolibarr_main_db_type='mysqli';
```

I tested the MySQL password for larissa SSH, and it worked. user.txt was in the larissa folder.

## Privilege Escalation

After logging in to the larissa account via SSH, I downloaded linpeas.sh and found a vulnerability for SUID:

```
                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════
                      ╚════════════════════════════════════╝
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
-rwsr-xr-x 1 root root 15K Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-sr-x 1 root root 15K Apr  8 18:36 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-x 1 root root 27K Jan 29  2020 /usr/lib/x86_64-linux-gnu/enlightenment/utils/enlightenment_sys (Unknown SUID binary!)
-rwsr-xr-x 1 root root 15K Jan 29  2020 /usr/lib/x86_64-linux-gnu/enlightenment/utils/enlightenment_ckpasswd (Unknown SUID binary!)
-rwsr-xr-x 1 root root 15K Jan 29  2020 /usr/lib/x86_64-linux-gnu/enlightenment/utils/enlightenment_backlight (Unknown SUID binary!)
-rwsr-xr-x 1 root root 15K Jan 29  2020 /usr/lib/x86_64-linux-gnu/enlightenment/modules/cpufreq/linux-gnu-x86_64-0.23.1/freqset (Unknown SUID binary!)
```

After researching, I found CVE-2022-37706 and used an exploit to gain root access.
