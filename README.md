# Blind SQL Injection Multi-Tool

This is a Python script I built to automate data extraction for three different types of **Blind SQL Injection** vulnerabilities. I designed this tool specifically to solve the Blind SQLi labs on **PortSwigger's Web Security Academy**. Instead of creating a separate script for each challenge, I combined everything into a single, clean tool where you can choose the mode using a simple flag.

The script uses a **Binary Search** algorithm to guess the password characters, which makes the execution much faster than guessing one by one.

## Supported Labs / Modes

*   **`conditional`** – For the *Blind SQL injection with conditional responses* lab (looks for specific text like "Welcome back").
*   **`errors`** – For the *Blind SQL injection with conditional errors* lab (triggers a database error to verify characters).
*   **`time`** – For the *Blind SQL injection with time delays and information retrieval* lab (uses database sleep functions to measure time delays).

## How to Run It

Open your terminal (CMD, PowerShell, or Kali) and run the script with the following arguments:

```bash
python exploit.py -u <URL> -t <TRACKING_ID_COOKIE> -s <SESSION_COOKIE> -m <MODE>
Example for Time Mode:
python exploit.py -u "[https://example.web-security-academy.net/](https://example.web-security-academy.net/)" -t "XYZ123" -s "ABC456" -m time

## Proof of Concept
![Password Extraction in Action](https://github.com/alisip-3/Omni-Blind-SQLi/blob/main/cmd_exploit.png)
![Lab Solved](https://github.com/alisip-3/Omni-Blind-SQLi/blob/main/lab_solved.png)
