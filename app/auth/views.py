from . import auth
from flask import render_template
from .forms import SignInForm, SignUpForm
from flask.ext.login import login_user, logout_user, current_user
from flask import render_template, redirect, url_for, request, flash, session
from . import auth
from .. import db
from ..model import User


@auth.route('/sign_in', methods=['GET', 'POST'])
def login():
    user_form = SignInForm()
    if user_form.validate_on_submit():
        user = User.query.filter_by(email=user_form.email.data).first()
        if user is not None and user.verify_password(user_form.password.data):
            login_user(user, user_form.remember_me.data)
            if current_user.role == "user":
                return redirect(request.args.get('next') or url_for('main.base'))
            else:
                return redirect(request.args.get('next') or url_for('main.admin_home'))
            
        flash("Invalid username or password")
    return render_template('auth/login.html', user_form=user_form)

@auth.route('/sign_up', methods=['GET', 'POST'])
def signup():
    user_form = SignUpForm()
    if user_form.validate_on_submit():
        user = User(first_name=user_form.first_name.data,
            last_name=user_form.last_name.data,
            email=user_form.email.data,
            phone_number=user_form.phone_number.data,
            password=user_form.password.data,
            role="user")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', user_form=user_form)

@auth.route('/sign_out')
def sign_out():
    logout_user()
    return redirect(url_for('auth.login'))