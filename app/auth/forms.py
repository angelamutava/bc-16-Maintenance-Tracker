from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..model import User
from wtforms import ValidationError

class SignInForm(Form):

	email = StringField('Email', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Sign In')

class SignUpForm(Form):

	first_name = StringField('FirstName', validators=[Required(), Length(1, 20)])
	last_name = StringField('LastName', validators=[Required(), Length(1, 20)])
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	phone_number = StringField('PhoneNumber', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required(), EqualTo('conf_password', message='Passwords must match.')])
	conf_password = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Sign Up')

	
	def validate_email(self, field):
		
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	