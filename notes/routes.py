from flask import render_template
from . import app, db
from flask_login import current_user, login_user, logout_user

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")