from flask import render_template, redirect, url_for, request, flash
from .cruds import LogUser
from werkzeug.security import generate_password_hash, check_password_hash
from mainapp import app
from mainapp import db
from flask_login import login_user, logout_user, login_required

@app.route('/login')
def login():
	return render_template('index.html')