# Penetration Test Report - Soccer Machine

## Initial Reconnaissance
- Initiated a nmap scan on the target machine and identified a web server running under the domain soccer.htb.
- Added the domain soccer.htb to /etc/hosts for easier access.
- Accessed the web domain and performed a directory brute force, revealing a vulnerable file manager (Tiny ver. 2.4.3).

## Exploitation
- Utilized an exploit to gain unauthorized access to the Tiny file manager, allowing for the upload of a shell.
- Accessed the server through the shell with the www-data user.
- Discovered a file containing the key, but it had read permissions only for the user player or root.

## Enumeration and Discovery
- Ran the linpeas.sh script to gather information and identified another server on a different domain of the machine.
- Added the domain soc-player.soccer.htb to /etc/hosts.
- Accessed this domain and observed it as the same site but with new functionalities, running in production.

## Web Application Exploitation
- Created an account and logged into the site.
- Discovered a form within the site using sockets to fetch data.
- Developed a Python script to create an HTTP API for the ws service.
- Utilized the HTTP API to perform SQL injection using sqlmap, revealing vulnerabilities.
- Obtained the player platform's username and password from the SQL injection results.

## Access to SSH
- Tested the obtained credentials for SSH access and successfully gained entry.

## Conclusion
This penetration test involved a multi-step approach, starting with web server reconnaissance, exploiting a vulnerable file manager, and progressing to a more sophisticated attack on a related service. The combination of web exploitation techniques and SQL injection ultimately granted access to the target machine.

*Note: This report is for educational purposes and should only be used in compliance with ethical hacking practices.*