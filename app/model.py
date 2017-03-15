from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import current_app
from . import login_manager
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	owner_id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True, index=True)
	phone_number = db.Column(db.String(64))
	role = db.Column(db.String(64))
	password_hash = db.Column(db.String(128))


	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

class Items():
	__tablename__ = "items"
	item_id = db.Column(db.Integer, primary_key=True)
	item_name = db.Column(db.String(64))
	status = db.Column(db.String(64))
	assigned_to = db.Column(db.String(64), default=False)