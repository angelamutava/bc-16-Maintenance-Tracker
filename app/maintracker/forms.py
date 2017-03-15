from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms import ValidationError
from wtforms.validators import Required



class MaintananceForm(Form):
	item_name = StringField('Item Name', validators=[Required()])
	item_issue = StringField('Item Issue', validators=[Required()])
	item_type = StringField('Item Type', validators=[Required()])
	status = SelectField(
        'Status',
        choices=[('good', 'Good'), ('needs repair', 'Needs Repair'), ('Under Repair', 'Under Repair')]
    )
	submit = SubmitField('Raise')