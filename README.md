# Web Security Toolbox

This is a collection of two Python tools I built while learning web penetration testing. Instead of just running ready-made tools like SQLMap without understanding what happens behind the scenes, I wanted to build my own scripts from scratch to really learn how these vulnerabilities work.

It started as a script to automate and solve hard labs on **PortSwigger's Web Security Academy**, and then I upgraded it into a custom scanner to test real-world websites for security issues.

## Project Structure

*   `exploit.py` – A targeted script that exploits Blind SQL Injection vulnerabilities and automatically solves the lab challenges.
*   `web_scanner.py` – A broader tool built as an upgrade to scan any URL for common security issues and bad configurations.

---

## 1. Blind SQLi Multi-Tool (`exploit.py`)

I wrote this script to automate data extraction for three different **Blind SQL Injection** labs on PortSwigger. Instead of writing a new script for every single lab, I combined them into one tool where you just choose the mode with a flag.

To make it fast, the script uses a **Binary Search** algorithm to guess the administrator's password character by character. 

### What makes it cool:
The script does not just print the password on your screen. Once it successfully extracts the full password, it automatically sends a login request to the target site, logs in as the administrator, and triggers the "Lab Solved" status on the server.

### Supported Modes
*   **`conditional`** – For the *Blind SQL injection with conditional responses* lab.
*   **`errors`** – For the *Blind SQL injection with conditional errors* lab.
*   **`time`** – For the *Blind SQL injection with time delays and information retrieval* lab.

### How to Run It
```bash
python exploit.py -u <URL> -t <TRACKING_ID_COOKIE> -s <SESSION_COOKIE> -m <MODE>
```
### Proof of Concept
![Here is the script running the binary search and solving the lab:](https://github.com/alisip-3/Web-Security-Toolbox/blob/main/cmd_exploit.png)

![And here is the confirmation from PortSwigger showing the lab is solved:](https://github.com/alisip-3/Web-Security-Toolbox/blob/main/lab_solved.png)

## 2. Custom Web Vulnerability Scanner ('web_scanner.py')
After finishing the PortSwigger labs, I wanted to upgrade the project. I wanted a tool that isn't just for one specific challenge, but something I can run against any URL to look for common web vulnerabilities.

This scanner takes a URL and checks for layout configurations and basic input flaws.

## What it checks:
Missing Security Headers – It scans the HTTP response to see if critical protective headers are missing (like CSP, X-Frame-Options, or HSTS).

**Information Disclosure**  – It checks if the server is leaking its exact type and software version (like an old Nginx banner), which helps attackers find known exploits.

**Basic XSS & SQLi** – It injects simple payloads into URL parameters to check if the server reflects the input or throws database error messages.

## How to Run It
Bash
python web_scanner.py -u "[http://example.com](http://example.com)"


### Proof of Concept
![Here is the scanner finding missing headers and an outdated server banner on a test website:](https://github.com/alisip-3/Web-Security-Toolbox/blob/main/web_scanner.png)
