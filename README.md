PROJECT: PyGuard - Interactive Security Laboratory
The application features three distinct modules:
1. Social Engineering: A "Homograph Attack" simulator mimicking a Microsoft login.
2. SQL Injection: A "Capture The Flag" (CTF) arena to practice database exploitation.
3. Data Encryption: A real-time AES-128 encryption/decryption playground.

[ PREREQUISITES ]
- Python 3.x
- pip (Python Package Installer)

[ INSTALLATION INSTRUCTIONS ]
1. Unzip the project folder.
2. Open a terminal/command prompt inside the folder.
3. Create a virtual environment (optional but recommended):
   python -m venv venv
   (Windows): venv\Scripts\activate
   (Mac/Linux): source venv/bin/activate

4. Install dependencies:
   pip install Flask cryptography

[ HOW TO RUN ]
1. Run the application:
   python app.py

2. Open your web browser and navigate to:
   http://127.0.0.1:5000

[ MODULE WALKTHROUGH ]

1. Phishing Simulator:
   - Compare the "Safe" link vs. the "Phishing" link.
   - Note the URL difference (rnicrosoft.com).
   - Enter dummy credentials in the Phishing link to see the "Hacked" screen.

2. SQL Injection Arena:
   - Navigate to the SQL Injection module.
   - Target: The Bank User Search.
   - Attack Payload: admin' OR '1'='1
   - Goal: Retrieve the hidden 'FLAG{...}' from the admin row and submit it.

3. Encryption Playground:
   - Type text to encrypt it using Fernet (AES).
   - Copy the ciphertext and decrypt it back to verify integrity.


[ SCREENSHOTS ]
<img width="1913" height="1047" alt="image" src="https://github.com/user-attachments/assets/44674256-e74f-4d1a-b7cc-7b5c7362d356" />
<img width="1916" height="1068" alt="image" src="https://github.com/user-attachments/assets/af28885e-433c-4d91-a3c5-c2a20ac3bf27" />
<img width="1916" height="1060" alt="image" src="https://github.com/user-attachments/assets/abbfd4b7-0fad-4f0b-96b1-f4d21c979e9b" />
<img width="1919" height="1063" alt="image" src="https://github.com/user-attachments/assets/524146d3-920b-47c1-b697-512b7877955e" />
<img width="1919" height="1051" alt="image" src="https://github.com/user-attachments/assets/a1ccb2ed-b473-4c71-b20d-e3eced424844" />


[ TECH STACK ]
- Backend: Python 3, Flask
- Database: SQLite3
- Frontend: HTML5, CSS3, Bootstrap 5
- Cryptography: Fernet (symmetric encryption)

==============================================================================
© 2025 PyGuard Security Lab Built by Abdullah
==============================================================================
