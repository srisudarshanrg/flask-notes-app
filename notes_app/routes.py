from notes_app import app, db
from notes_app.forms import LoginForm, RegisterForm
from notes_app.models import User, Note
from flask import render_template
from flask_login import login_required, current_user

@app.route("/")
@app.route("/notes", methods=["GET", "POST"])
@login_required
def notes_app():
    return render_template("home.html")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    return render_template("profile.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)

@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    return render_template("register.html", form=register_form)
