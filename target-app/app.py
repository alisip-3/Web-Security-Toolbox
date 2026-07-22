import re
import socket
from flask import Flask, render_template, request, redirect, make_response
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def log_security_event(event_type, ip_address, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{event_type}] IP: {ip_address} | {details}\n"
    with open("security.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    CORRECT_USER = "admin"
    CORRECT_PASS = "12345"
    
    if username == CORRECT_USER and password == CORRECT_PASS:
        resp = make_response(redirect(f"/secure-zone/bank?user={username}"))
        resp.set_cookie('session_token', 'secure_user_session_12345') 
        return resp
    else:
        # Returns back to the login page with a clean error message
        return render_template("login.html", error="Invalid username or password!")

@app.route("/secure-zone/bank")
def bank_dashboard():
    return render_template("bank.html")

@app.route("/log", methods=['GET', 'POST'])
def log_data():
    try: # Added try/except for robustness
        if request.args:
            print(f"\n--- [!] New data received (GET) ---")
            for key, value in request.args.items():
                # Simple sanitization using re.sub
                clean_value = re.sub(r'[^a-zA-Z0-9.\-_\/=&]', '', value)
                print(f"{key}: {clean_value}")
                log_security_event("EXFILTRATION", request.remote_addr, f"{key}: {clean_value}")
        return "OK", 200
    except: # Silently handle any unexpected request errors
        return "OK", 200

if __name__ == "__main__":
    # Standard setup
    app.run(debug=True, port=5000)
