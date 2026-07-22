# AI-Powered Vulnerability Reporter

##  Overview
An automated Proof-of-Concept (PoC) and reporting tool that identifies web vulnerabilities, captures visual evidence, and generates professional penetration testing reports using a local Large Language Model (Ollama). Inspired by **PortSwigger Web Security Academy** labs on Authentication and Session Management, this tool targets a custom-built **Flask** web application. 

Instead of manually writing reports after finding a bug, this tool automates the exploitation, takes a screenshot of the compromised state, and uses a local AI to generate a structured, remediation-focused report.

## Live Demo
**⚠️ WARNING: This is an intentionally vulnerable application for educational purposes only!**

- **Banking Application**: https://python-pickwiz.onrender.com
- **Test Credentials**: `admin` / `12345`

## Features & Workflow
1. **Automate Exploitation**: Playwright launches a headless browser and injects a hardcoded session cookie to bypass Broken Access Control on the `/secure-zone/bank` endpoint.
2. **Capture Evidence**: If successful, the script automatically takes a screenshot of the compromised dashboard to serve as undeniable Proof of Concept (PoC).
3. **AI Reporting**: Sends the technical findings to a local Ollama instance to generate a structured Markdown report featuring an Executive Summary, Business Impact, and Remediation code snippets.


## 🛠️ Tech Stack
- **Target Application**: Python Flask 
- **Browser Automation**: Playwright (Async Python)
- **AI Integration**: Ollama (Llama 3.2)


## How It Works
1. **Targeting**: The script targets a specific endpoint (e.g., `/secure-zone/bank`).
2. **Exploitation**: Playwright injects a known vulnerable cookie (`session_token=secure_user_session_12345`) and navigates to the page.
3. **Evidence Capture**: If the page loads successfully (HTTP 200), a screenshot (`proof_of_exploit.png`) is saved.
4. **AI Analysis**: The script sends the technical findings to the local Ollama instance with a strict prompt template.
5. **Report Generation**: A comprehensive Markdown report (`vulnerability_report.md`) is generated, embedding the screenshot and providing developer-friendly fixes.

## Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
- The `llama3.2` model downloaded (`ollama pull llama3.2`)


## 🚀 Quick Start
```bash
git clone https://github.com/alisip-3/AI-Powered-Vulnerability-Reporter.git
cd AI-Powered-Vulnerability-Reporter
pip install -r requirements.txt
playwright install chromium
python main.py
```


## Example Output: 
When executed successfully, the tool generates a professional report. The "Technical Details" section will automatically render the captured proof:

![](https://github.com/alisip-3/AI-Powered-Vulnerability-Reporter/blob/main/output/proof_of_exploit.png)


## Lessons Learned
- **Discovery vs. Automation:** While automated scanners are great, understanding how to manually discover a vulnerability (e.g., inspecting network traffic for static cookies) is crucial before automating the PoC.
- **Prompt Engineering:** Getting a useful report from an LLM requires strict prompting. Defining the exact output structure (Executive Summary, Impact, Remediation) prevents the AI from generating generic, unhelpful text.
- **Error Handling:** Integrating headless browsers requires robust timeout and state-waiting logic to handle real-world network latency (especially on free-tier hosting like Render).

# Disclaimer
This project is for educational and portfolio purposes only. Always ensure you have explicit permission before testing any application.

