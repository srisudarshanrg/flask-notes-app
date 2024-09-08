from notes_app import app, db
from notes_app.forms import LoginForm, RegisterForm
from notes_app.models import User, Note
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from notes_app.functions import HashPassword, CheckPasswordHash

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
    if login_form.validate_on_submit():
        credential_entered = login_form.credential.data
        password_entered = login_form.password.data

        attempted_user_username = User.query.filter_by(username=credential_entered).first()
        attempted_user_email = User.query.filter_by(email=credential_entered).first()
        if attempted_user_username and CheckPasswordHash(attempted_user_username.password, bytes(password_entered, "utf-8")):
            login_user(attempted_user_username)
            flash(message="You have been registered logged in successfully", category="info")
            return redirect(url_for("notes_app"))
        elif attempted_user_email and CheckPasswordHash(attempted_user_email.password, bytes(password_entered, "utf-8")):
            login_user(attempted_user_username)
            flash(message="You have been registered logged in successfully", category="info")        
            return redirect(url_for("notes_app"))
        else:
            flash(message="Incorrect Credentials", category="danger")

    return render_template("login.html", form=login_form)

@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        username_entered = register_form.username.data
        email_entered = register_form.email.data

        check_username = User.query.filter_by(username=username_entered).all()
        check_email = User.query.filter_by(email=email_entered).all()

        if len(check_username) > 0:
            flash(message="This username already exists", category="danger")
        elif len(check_email) > 0:
            flash(message="This email address already exists", category="danger")
        elif len(check_username) > 0 and len(check_email) > 0:
            flash(message="This username and email address already exists.", category="danger")
        else:
            hashed_password = HashPassword(password=register_form.password.data)
            new_user = User(
                username=username_entered,
                email=email_entered,
                password=hashed_password,
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            flash(message="You have been registered and logged in successfully", category="info")

            return redirect(url_for("notes_app"))

    return render_template("register.html", form=register_form)
