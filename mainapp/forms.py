from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField,TextField,DateField,RadioField
from wtforms.validators import DataRequired, Length

class AdmissionForm(FlaskForm):
	name = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email*')
	dob = DateField('Your Date of Birth', validators=[DataRequired()], format='%Y-%m-%d')
	gender=RadioField('Label', choices=[('m','Male'),('fm','Female'),('othr','Others')])
	nationality=RadioField('Label', choices=[('indian','Indian'),('nri','NRI')])
	fathername = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)])
	phno= StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)])
	
	age= IntegerField('Age*')
	classval= SelectField('Class*', choices=[('nur', 'Nursery'), ('lkg', 'LKG'), ('ukg', 'UKG'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')]) 
	address = StringField('Address*',validators=[DataRequired(),Length(min=10)])
	submit= SubmitField('Submit')


class ContactForm(FlaskForm):

	fname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "First Name"})
	lname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Last Name"})
	email = StringField('Email*',validators=[DataRequired()],render_kw={"placeholder": "Email"})
	phno = StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)],render_kw={"placeholder": "Phone No."})
	message= TextField('Message*',validators=[DataRequired()],render_kw={"placeholder": "Message"})
	submit= SubmitField('Submit your query')