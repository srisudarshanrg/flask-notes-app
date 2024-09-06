from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    credential = StringField(label="Username or Email", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=15)])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = StringField(label="Password", validators=[DataRequired()])
    password_confirm = StringField(label="Confirm Password", validators=[DataRequired(), EqualTo(fieldname="password")])
    submit = SubmitField(label="Submit")

