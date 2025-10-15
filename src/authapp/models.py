"""
Filename: models.py
Title: M2_Act_2
Description: Full Stack Foundations: Flask, SQLAlchemy, and MySQL Integration
Author: Colorado Online
Student Name: [Enter your full name here]
"""
from authapp import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    about = db.Column(db.String)
    passwd = db.Column(db.LargeBinary)
