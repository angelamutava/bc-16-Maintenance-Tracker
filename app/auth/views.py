from . import auth
from flask import render_template






@auth.route('/sign_in', methods=['GET', 'POST'])
def login():
	return render_template('auth/login.html')


@auth.route('/sign_up', methods=['GET', 'POST'])
def signup():
	return render_template('auth/signup.html')
