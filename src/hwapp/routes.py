"""
Filename: __init__.py
Title: M2_Act_2
Description: Full Stack Foundations: Flask, SQLAlchemy, and MySQL Integration
Author: Colorado Online
Student Name: [Enter your full name here]
"""
from hwapp import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"