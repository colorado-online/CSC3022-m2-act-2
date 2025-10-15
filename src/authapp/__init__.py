"""
Filename: __init__.py
Title: M2_Act_2
Description: Full Stack Foundations: Flask, SQLAlchemy, and MySQL Integration
Author: Colorado Online
Student Name: [Enter your full name here]
"""
from flask import Flask
import os

app = Flask("Authentication Web App")
app.secret_key = os.environ['SECRET_KEY']

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@localhost/m2act2db'
db.init_app(app)

from authapp import models
with app.app_context(): 
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from authapp.models import User

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from authapp import routes