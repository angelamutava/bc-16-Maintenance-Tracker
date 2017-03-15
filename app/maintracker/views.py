from . import main
from flask import render_template






@main.route('/')
@main.route('/home')
def home_page():
	return render_template('maintracker/base.html')