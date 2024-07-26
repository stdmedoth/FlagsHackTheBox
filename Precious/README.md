# Penetration Test Report - Precious Machine

## Initial Scanning and Enumeration
- Conducted network scanning using nmap.
- Discovered an HTTP service running on port 80.
- Associated the machine's IP with the domain precious.htb.

## Web Application Analysis
- Explored the website on port 80, which generated PDFs from web pages.
- Linked the machine's IP to the domain precious.htb.
- Observed the site returning a base64-encoded PDF when a server's URL was provided.
- Decoded the PDF, revealing the use of pdfkit v0.8.6 for PDF generation.
- Identified a vulnerability in the pdfkit version allowing command injection via the URL.
- Exploited the vulnerability to upload a shell (user: ruby) from my machine.
- Discovered user.txt with read permissions restricted to the user henry and root.

## User Escalation
- Enhanced access with a meterpreter interface and ran linpeas.sh for system information.
- Found the file /home/ruby/.bundle/config containing the user henry's password for ruby bundle configuration.
  ```
  user: henry
  pass: Q3c1AqGHtoI0aXAYFH
  ```
- Tested the bundle password for SSH with user henry and successfully gained access.
- Retrieved user.txt with the flag.

## Root Escalation
- linpeas.sh reported the ability to use sudo on a Ruby package update file.
- Created a payload file based on information from https://staaldraad.github.io/post/2021-01-09-universal-rce-ruby-yaml-load-updated/.
- Executed the package update with the payload, gaining root-level command execution.
- Obtained root.txt with the flag.

## Conclusion
This penetration test demonstrated a step-by-step compromise of the Precious machine, starting from web exploitation, user escalation, and finally, root escalation. The exploitation involved leveraging vulnerabilities in the PDF generation process and exploiting sudo permissions to achieve full compromise.

*Note: This report is for educational purposes and should only be used in compliance with ethical hacking practices.*