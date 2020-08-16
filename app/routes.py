from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from flask_mail import Message

from app import app, db, login, mail
from app.forms import LoginForm, RegisterForm, ResetPasswordForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.j2', form=form)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        msg = Message('Hello: [password_reset_link]', sender='no-reply@rafl.cf', recipients=[form.email.data])
        mail.send(msg)
        flash('A password reset link has been sent to your email.')
        return redirect(url_for('login'))
    return render_template('reset_password.j2', form=form)
        

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.j2', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
