# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify([{"nama": "Hello, ini dibuat oleh Anggel Aurelin"}, 
                    {"nim":"2119113948"},
                    {"jurusan":"Sistem Informasi"},
                    {"mata kuliah":"Komputasi Awan"}
                    
                    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
