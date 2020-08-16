from flask import flash, url_for
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, Optional, ValidationError)

from app.models import User

USERNAME_MIN_LEN = 4
USERNAME_MAX_LEN = 16

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 16

EMAIL_MAX_LEN = 120

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=USERNAME_MIN_LEN, max=USERNAME_MAX_LEN)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=USERNAME_MIN_LEN, max=USERNAME_MAX_LEN)])
    email = StringField('Email (optional)', validators=[Optional(), Email(), Length(max=EMAIL_MAX_LEN)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN), EqualTo('password_repeat')])
    password_repeat = PasswordField('Repeat Password')
    submit = SubmitField('Register')

    def validate_email(self, email):
        print('called validate_email')
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email is already associated with an account.<br>Forgot your password? <a href="{}">Click here!</a>'.format(url_for('reset_password')))

    def validate_username(self, username):
        print('called validate_username')
        user = User.query.filter_by(username=username.data).first()
        print('User is:', user)
        if user is not None:
            raise ValidationError('The username is already taken.')

class ResetPasswordForm(FlaskForm):
    email = StringField('Email (optional)', validators=[DataRequired(), Email(), Length(max=EMAIL_MAX_LEN)])
    submit = SubmitField('Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There exists no account with this email.')
