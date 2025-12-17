import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet

app = Flask(__name__)

# --- CONFIGURATION ---
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)
DATABASE = 'pyguard.db'

# --- DATABASE SETUP ---
def init_db():
    """Initializes the database with CTF data."""
    if os.path.exists(DATABASE):
        try:
            os.remove(DATABASE)
            print(f"⚠️ Old {DATABASE} removed to refresh data.")
        except:
            pass

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, secret_data TEXT)''')
    
    # CTF Data Seeding
    users = [
        ('admin', 'FLAG{SQL_INJECTION_MASTER_2025}'),
        ('Abdullah', 'Account Balance: $12,500'),
        ('Sana', 'Pending Transaction: -$500'),
        ('Paul', 'Note: Change password soon')
    ]
    c.executemany('INSERT INTO users (username, secret_data) VALUES (?, ?)', users)
    conn.commit()
    conn.close()
    print(f"✅ Database initialized successfully at: {os.path.abspath(DATABASE)}")

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

# MODULE 1: SOCIAL ENGINEERING
@app.route('/legit_login', methods=['GET', 'POST'])
def legit_login():
    if request.method == 'POST':
        return redirect(url_for('office_dashboard'))
    return render_template('legit_login.html')

@app.route('/office_dashboard')
def office_dashboard():
    return render_template('dashboard_lite.html')

@app.route('/phishing', methods=['GET', 'POST'])
def phishing():
    if request.method == 'POST':
        captured_user = request.form.get('email')
        captured_pass = request.form.get('password')
        return render_template('hacked.html', user=captured_user, pwd=captured_pass)
    return render_template('phishing.html')

# MODULE 2: SQL INJECTION
@app.route('/sqli', methods=['GET', 'POST'])
def sqli():
    result = None
    query_executed = ""
    error = None
    
    if request.method == 'POST':
        username_input = request.form.get('username')
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        try:
            # VULNERABLE QUERY FOR DEMO
            query_executed = f"SELECT * FROM users WHERE username = '{username_input}'"
            cursor = c.execute(query_executed)
            result = cursor.fetchall()
        except Exception as e:
            error = str(e)
        finally:
            conn.close()

    return render_template('sqli.html', result=result, query=query_executed, error=error)

@app.route('/check_flag', methods=['POST'])
def check_flag():
    user_flag = request.form.get('flag_submission')
    if user_flag == "FLAG{SQL_INJECTION_MASTER_2025}":
        return "CORRECT"
    return "WRONG"

# MODULE 3: ENCRYPTION
@app.route('/encryption', methods=['GET', 'POST'])
def encryption():
    original = ""
    encrypted = ""
    decrypted = ""
    
    if request.method == 'POST':
        action = request.form.get('action')
        text = request.form.get('text_input')
        if action == 'encrypt' and text:
            original = text
            encrypted = cipher_suite.encrypt(text.encode()).decode()
        elif action == 'decrypt' and text:
            try:
                decrypted = cipher_suite.decrypt(text.encode()).decode()
                encrypted = text
            except:
                decrypted = "Error: Invalid Token"

    return render_template('encryption.html', original=original, encrypted=encrypted, decrypted=decrypted)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)