# Report

## Port Discovery with Nmap

First of all, I used Nmap and discovered ports 80 and 21.

```plaintext
Starting Nmap 7.80 ( https://nmap.org ) at 2024-07-22 00:59 -03
Host is up (0.14s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: eLEARNING
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.63 seconds
```

## Vulnerability Scanning

I scanned for vulnerabilities but found nothing. After trying many things, such as HTTP server vulnerability checks and URL path brute force, I attempted a DNS brute force using FUZZ.

```plaintext
ffuf -w ../wordists/subdomains-top1million-20000.txt -H "Host: FUZZ.permx.htb" -u http://10.10.11.23 -fw 18
```

This returned:
```plaintext
www                     [Status: 200, Size: 36178, Words: 12829, Lines: 587]
lms                     [Status: 200, Size: 19347, Words: 4910, Lines: 353]
```

## Discovery of Chamilo Application

The new domain has an application called Chamilo. After searching for vulnerabilities in this application, I found an RCE vulnerability.

I downloaded `chamilo-lms-unauthenticated-big-upload-rce-poc` and received a reverse TCP communication.

## Accessing the mtz User Folder

I found the Chamilo application folder, where there is the configuration file. In this file, I found the username and password for the Chamilo database.

I tried the password with user mtz on SSH and BAAAM! The `user.txt` file was in the `/home/mtz` folder.

