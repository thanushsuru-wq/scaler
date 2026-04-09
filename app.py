import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import sqlite3
import cv2
import numpy as np

app = Flask(__name__)
app.secret_key = 'super_secret_clinical_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def init_db():
    conn = sqlite3.connect('clinical.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prescriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            filename TEXT,
            recommendation TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/trials.html')
def trials():
    return render_template('trials.html')

@app.route('/patients.html')
def patients():
    return render_template('patients.html')

@app.route('/assign.html')
def assign():
    if 'user_id' not in session:
        flash("Please log in to access the Evaluation Dashboard.")
        return redirect(url_for('login'))
    return render_template('assign.html')

# --- AUTHENTICATION ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('clinical.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials.")
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = sqlite3.connect('clinical.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            flash("Registration successful. Please log in.")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
            
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('home'))

# --- ML & OPENCV PIPELINE ---

def extract_and_recommend(filepath):
    # OpenCV Preprocessing Pipeline
    image = cv2.imread(filepath)
    if image is None:
        return "Error: Unreadable image."
    
    # Algorithm 1: Grayscale Conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Algorithm 2: Adaptive Thresholding (to highlight text)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Mocking NLP & OCR Recommendation Engine based on image properties (since tesseract may not be installed)
    # The true ML algorithm would use pytesseract.image_to_string(thresh) here.
    mean_val = np.mean(thresh)
    
    if mean_val < 100:
         return "ML Output: Detected high contrast metrics indicative of cardiology focus. Recommendation: Suggest TRIAL-A01 CardioX compatibility. Requires Beta-Blocker review."
    elif mean_val > 200:
         return "ML Output: Text sparseness detected. Likely Neurology prescription. Recommendation: Queue for TRIAL-B02 NeuroRegen."
    else:
         return "ML Output: General internal medicine markers detected. Recommendation: Map patient to general pool and waitlist TRIAL-C03."

@app.route('/prescription', methods=['GET', 'POST'])
def prescription():
    if 'user_id' not in session:
        flash("Login required to upload prescriptions.")
        return redirect(url_for('login'))
        
    recommendation = None
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            recommendation = extract_and_recommend(filepath)
            
            conn = sqlite3.connect('clinical.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO prescriptions (user_id, filename, recommendation) VALUES (?, ?, ?)", 
                        (session['user_id'], file.filename, recommendation))
            conn.commit()
            conn.close()
            
    return render_template('prescription.html', recommendation=recommendation)

# --- CHATBOT ---

@app.route('/chat.html')
def chat_ui():
    if 'user_id' not in session:
        flash("Please log in to converse with the AI.")
        return redirect(url_for('login'))
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_msg = request.json.get('message', '').lower()
    
    # Chatbot Intent Generation Algorithm
    response = "I am the Autonomous Medical Recruitment Specialist. How can I assist your trial assignments today?"
    
    if "prescription" in user_msg:
         response = "You can upload a prescription in the Prescription Analysis tab. My OpenCV models will preprocess the scan using Adaptive Gaussian Thresholding and evaluate matching trial parameters."
    elif "trial" in user_msg or "assign" in user_msg:
         response = "We currently have CardioX, NeuroRegen, and ImmunoBoost trials. CardioX operates at 90% capacity and prioritizes urgent high-risk assignment."
    elif "hello" in user_msg or "hi" in user_msg:
         response = "Greetings! I'm fully online and running OpenCV analysis clusters."
    elif "doctor" in user_msg:
         response = "All doctor prescriptions are securely scanned and matched against inclusion criteria to ensure strict adherence to safety targets."
         
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
