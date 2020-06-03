from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired, Length

class AdmissionForm(FlaskForm):
	name = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)])
	phno= StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)])
	email = StringField('Email*',validators=[DataRequired()])
	age= IntegerField('Age*')
	classval= SelectField('Class*', choices=[('nur', 'Nursery'), ('lkg', 'LKG'), ('ukg', 'UKG'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')]) 
	address = StringField('Address*',validators=[DataRequired(),Length(min=10)])
	submit= SubmitField('Submit')