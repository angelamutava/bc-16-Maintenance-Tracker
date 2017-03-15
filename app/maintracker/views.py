from . import main
from flask import render_template
from .forms import MaintananceForm
from ..model import User, Items
from .. import db
from flask import render_template, redirect, url_for, request, flash, session
from flask.ext.login import logout_user, current_user, login_required






@main.route('/')
@main.route('/home')
def home_page():
	return render_template('maintracker/home.html')



@main.route('/base', methods=['GET', 'POST'])
@login_required
def base():
	maintanances = (Items.query.filter_by(raised_by=current_user.email))
	approved = (Items.query.filter_by(status='Good').all())
	return render_template('base.html', maintanances=maintanances, approved=approved)

@main.route('/maintanance', methods=['GET', 'POST'])
@login_required
def maintanance():
	main_form = MaintananceForm()
	if main_form.validate_on_submit():
		main = Items(item_name=main_form.item_name.data,
			
			item_type=main_form.item_type.data,
			status=main_form.status.data,
			raised_by=current_user.email)
		db.session.add(main)
		db.session.commit()
		flash("Maintanance request submitted successfully")
		return redirect(url_for('main.base'))
	return render_template('maintracker/maintanance.html', main_form=main_form)
	

@main.route('/admin_home', methods=['GET', 'POST'])
@login_required
def admin_home():
	maintanances = (Items.query.filter_by(status='Needs Repair').all())
	
	return render_template('admin/admin_home.html', maintanances=maintanances)



@main.route('/admin_mains', methods=['GET', 'POST'])
@login_required
def admin_mains():
	maintanances = Items.query.all()
	return render_template('admin/maintanance.html', maintanances=maintanances)


@main.route('/admin_users', methods=['GET', 'POST'])
@login_required
def admin_users():
	users = User.query.all()
	return render_template('admin/users.html', users=users)