"""
Filename: routes.py
Title: M2_Act_2
Description: Full Stack Foundations: Flask, SQLAlchemy, and MySQL Integration
Author: Colorado Online
Student Name: [Enter your full name here]
"""
from authapp import app, db
from authapp.models import User
from authapp.forms import SignUpForm, LoginForm
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

# TODO #1: implement the sign-up functionality:
# * if passwords match, generate a "salted" hashed password using bcrypt
# * instantiate a user object from form information
# * store the user information in the database (hint: use db.session)
# * redirect to index
@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    return 'Work in progress...'
    
# TODO #2: implement the login functionality:
# * query the database for the user with given id 
# * if passwords match, complete the login procedure
@app.route('/users/login', methods=['GET', 'POST'])
def login():
    return 'Work in progress...'

# TODO #3: implement the sign-out functionality
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    return 'Work in progress...'

@app.route('/users')
@login_required
def list_users(): 
    users = User.query.all()
    return render_template('users.html', users=users)