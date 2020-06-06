from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField,TextField
from wtforms.validators import DataRequired, Length

class AdmissionForm(FlaskForm):
	name = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)])
	phno= StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)])
	email = StringField('Email*')
	age= IntegerField('Age*')
	classval= SelectField('Class*', choices=[('nur', 'Nursery'), ('lkg', 'LKG'), ('ukg', 'UKG'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')]) 
	address = StringField('Address*',validators=[DataRequired(),Length(min=10)])
	submit= SubmitField('Submit')


class ContactForm(FlaskForm):
		"""docstring for ContactForm"FlaskFormef __init__(self, arg):
			super(ContactForm,FlaskForm.__init__()
			self.arg = arg"""
		fname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "First Name"})
		lname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Last Name"})
		email = StringField('Email*',validators=[DataRequired()],render_kw={"placeholder": "Email"})
		phno = StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)],render_kw={"placeholder": "Phone No."})
		message= TextField('Message*',validators=[DataRequired()],render_kw={"placeholder": "Message"})
		submit= SubmitField('Submit your query')