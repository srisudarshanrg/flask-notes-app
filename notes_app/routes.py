from notes_app import app, db
from flask import render_template
from flask_login import login_required, current_user

@login_required
@app.route("/")
@app.route("/notes", methods=["GET", "POST"])
def notes_app():
    return render_template("home.html")

@login_required
@app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("profile.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
