from . import main
from flask import render_template
from .forms import AddUserForm, ApproveForm, MaintananceForm, AssignForm
from ..model import User, Items, Assigned
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
    approved = (Items.query.filter_by(status="Under Repair"))
    assigned = (Items.query.filter_by(assigned_to=current_user.full_name))
    return render_template('base.html', maintanances=maintanances, approved=approved, assigned=assigned)


@main.route('/maintanance', methods=['GET', 'POST'])
@login_required
def maintanance():
    main_form = MaintananceForm()
    if main_form.validate_on_submit():
        main = Items(item_name=main_form.item_name.data,
            item_issue=main_form.item_issue.data,
            item_type=main_form.item_type.data,
            status=main_form.status.data,
            assigned_to="Not Assigned",
            raised_by=current_user.email)
        db.session.add(main)
        db.session.commit()
        flash("Maintanance request submitted successfully.")
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


@main.route('/approve/<int:id>', methods=['GET', 'POST'])
@login_required
def approve(id):
    item = Items.query.get_or_404(id)
    approve_form = ApproveForm()
    main_form = MaintananceForm()
    if approve_form.validate_on_submit():
        item.status = "Under Repair"
        item.comment = approve_form.comment.data
        db.session.add(item)
        db.session.commit()
        flash("Maintanance request submitted successfully")
        return redirect(url_for('main.admin_mains'))
    approve_form.item_name.data = item.item_name
    approve_form.item_issue.data = item.item_issue
    approve_form.item_type.data = item.item_type
    return render_template('admin/approvereject.html', approve_form=approve_form)


@main.route('/admin_add_user', methods=['GET', 'POST'])
@login_required
def admin_add_user():
    user_form = AddUserForm()
    if user_form.validate_on_submit():
        user = User(first_name=user_form.first_name.data,
            last_name=user_form.last_name.data,
            email=user_form.email.data,
            phone_number=user_form.phone_number.data,
            password=user_form.password.data,
            role="admin")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.admin_mains'))
    return render_template('admin/add_user.html', user_form=user_form)


@main.route('/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign(id):
    item = Items.query.get_or_404(id)
    assign_form = AssignForm(request.form)
    if assign_form.validate_on_submit():
        item.assign_to = assign_form.assignees.data
        db.session.commit()
        return redirect(url_for('main.admin_home'))

    return render_template('admin/assign.html', assign_form=assign_form, item=item, id=id)
