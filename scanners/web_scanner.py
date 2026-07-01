import argparse
import requests

#modern web headers
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]


def check_headers(url, headers):
    """ HTTP Headers test leak information or ani-defens"""
    print("\n[*] Scanning HTTP Headers...")
    missing_headers = []

    # mising headers test
    for header in SECURITY_HEADERS:
        if header not in headers:
            missing_headers.append(header)
            print(f"[-] MISSING: Security Header '{header}' is not set.")

    if not missing_headers:
        print("[✓] All basic security headers are present.")

    # Information Disclosure test
    server_header = headers.get("Server")
    powered_by = headers.get("X-Powered-By")

    if server_header:
        print(f"[!] INFO: Server banner revealed: {server_header}")
    if powered_by:
        print(f"[!] INFO: Technology stack revealed (X-Powered-By): {powered_by}")


def check_xss(url):
    """  Reflected XSS test url parameters """
    print("\n[*] Testing for basic Reflected XSS...")
    xss_payload = "<script>alert('XSS')</script>"

    # payload parameter test
    test_url = f"{url}?search={xss_payload}&q={xss_payload}"

    try:
        response = requests.get(test_url, timeout=10)
        if xss_payload in response.text:
            print(f"[+] VULNERABILITY FOUND: Potential Reflected XSS detected on {url}!")
            print(f"    Payload reflected in response body.")
        else:
            print("[-] No obvious XSS reflection found with simple payload.")
    except requests.exceptions.RequestException as e:
        print(f"[-] XSS scan failed: {e}")


def check_sqli(url):
    """test SQL Injection Error-Base"""
    print("\n[*] Testing for basic Error-Based SQLi...")
    sqli_payload = "'"
    test_url = f"{url}?id={sqli_payload}&user={sqli_payload}"

    # common words
    sql_errors = [
        "you have an error in your sql syntax",
        "unclosed quotation mark after the character string",
        "postgresql query failed",
        "oracle error",
        "mysql_fetch_array"
    ]

    try:
        response = requests.get(test_url, timeout=10)
        response_text_lower = response.text.lower()

        vulnerable = False
        for error in sql_errors:
            if error in response_text_lower:
                print(f"[+] VULNERABILITY FOUND: Potential SQL Injection detected!")
                print(f"    Database error signature found: '{error}'")
                vulnerable = True
                break

        if not vulnerable:
            print("[-] No database error signatures detected in response.")
    except requests.exceptions.RequestException as e:
        print(f"[-] SQLi scan failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="Custom Web Vulnerability Scanner for Students Portfolio.")
    parser.add_argument("-u", "--url", required=True, help="Target URL to scan (e.g., http://example.com)")
    args = parser.parse_args()

    target_url = args.url
    print("=" * 60)
    print(f"Starting Custom Web Vulnerability Scan on: {target_url}")
    print("=" * 60)

    try:
        # first try Headers requests
        response = requests.get(target_url, timeout=10)

        # runs test
        check_headers(target_url, response.headers)
        check_xss(target_url)
        check_sqli(target_url)

        print("\n[+] Scan complete.")
        print("=" * 60)

    except requests.exceptions.RequestException as e:
        print(f"[-] Failed to connect to the target URL: {e}")


if __name__ == "__main__":
    main()
