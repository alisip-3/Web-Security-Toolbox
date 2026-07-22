# AI-Powered Vulnerability Reporter

An automated Proof-of-Concept (PoC) and reporting tool that identifies web vulnerabilities, captures visual evidence, and generates professional penetration testing reports using a local Large Language Model (Ollama).

## Project Overview
This project was built to demonstrate the automation of a common security workflow: verifying a vulnerability and documenting it for developers. Instead of manually writing reports after finding a bug, this tool automates the exploitation, takes a screenshot of the compromised state, and uses a local AI to generate a structured, remediation-focused report.

## Features
- **Automated Exploitation**: Uses Playwright to simulate a browser, inject payloads (e.g., hardcoded session cookies), and verify Broken Access Control.
- **Visual Evidence**: Automatically captures a headless browser screenshot of the exploited state to serve as undeniable Proof of Concept (PoC).
- **Local AI Reporting**: Integrates with Ollama (Llama 3.2) to generate structured, professional vulnerability reports complete with Executive Summaries and secure code remediation examples.
- **Zero External API Dependencies**: All AI processing happens locally, ensuring sensitive vulnerability data never leaves the machine.

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

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Powered-Vuln-Reporter.git
   cd AI-Powered-Vuln-Reporter
   ```
   
2.Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3.Ensure Ollama is running in the background, then execute the script:
   ```bash
   python main.py
   ```

4.View the generated vulnerability_report.md in your IDE or GitHub to see the final output.



## Example Output: 
When executed successfully, the tool generates a professional report. The "Technical Details" section will automatically render the captured proof:

![](https://github.com/alisip-3/AI-Powered-Vulnerability-Reporter/blob/main/output/proof_of_exploit.png)


## Lessons Learned
- **Discovery vs. Automation:** While automated scanners are great, understanding how to manually discover a vulnerability (e.g., inspecting network traffic for static cookies) is crucial before automating the PoC.
- **Prompt Engineering:** Getting a useful report from an LLM requires strict prompting. Defining the exact output structure (Executive Summary, Impact, Remediation) prevents the AI from generating generic, unhelpful text.
- **Error Handling:** Integrating headless browsers requires robust timeout and state-waiting logic to handle real-world network latency (especially on free-tier hosting like Render).
# License
This project is for educational and portfolio purposes only. Always ensure you have explicit permission before testing any application.

