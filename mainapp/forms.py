from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField,TextField,DateField,RadioField
from wtforms.validators import DataRequired, Length

class AdmissionForm(FlaskForm):
	
	#Student Info
	name = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email*')
	dob = DateField('Date of Birth*', validators=[DataRequired()], format='%Y-%m-%d')
	gender=RadioField('Gender*', choices=[('m','Male'),('fm','Female'),('othr','Others')],validators=[DataRequired()])
	nationality=RadioField('Nationality*', choices=[('indian','Indian'),('nri','NRI')],validators=[DataRequired()])

	#parental Info

	fathername = StringField('Father Name*',validators=[DataRequired(),Length(min=2,max=20)])
	fage= IntegerField("Age*",validators=[DataRequired()])
	fedu = StringField('Education*',validators=[DataRequired(),Length(min=2,max=10)])
	fincome= IntegerField('Annual Income*',validators=[DataRequired()])
	fphno= StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)])
	
	mothername = StringField('Mother Name*',validators=[DataRequired(),Length(min=2,max=20)])
	mage= IntegerField("Age*",validators=[DataRequired()])
	medu = StringField('Education*',validators=[DataRequired(),Length(min=2,max=10)])
	mincome= IntegerField('Annual Income*',validators=[DataRequired()])
	mphno= StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)])
	
	guardianname = StringField('Guardian Name*',validators=[DataRequired(),Length(min=2,max=20)])
	gage= IntegerField("Age*",validators=[DataRequired()])
	gedu = StringField('Education*',validators=[DataRequired(),Length(min=2,max=10)])
	gincome= IntegerField('Annual Income*',validators=[DataRequired()])
	gphno= StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)])


	#Permanent address

	hldno=StringField('Holding No. / Quarters No. *',validators=[DataRequired()])
	city=StringField('City*',validators=[DataRequired()])
	dist=StringField('District*',validators=[DataRequired()])
	state=StringField('State*',validators=[DataRequired()])
	pin=StringField('PIN*',validators=[DataRequired(),Length(min=6,max=6)])
	ephno=StringField('Emergency Phone No.*',validators=[DataRequired(),Length(min=10,max=10)])
	mobile=StringField('Mobile*',validators=[DataRequired(),Length(min=10,max=10)])
	telphn=StringField('Telephone No.')

	#Temporary Address

	thldno=StringField('Holding No. / Quarters No. *',validators=[DataRequired()])
	tcity=StringField('City*',validators=[DataRequired()])
	tdist=StringField('District*',validators=[DataRequired()])
	tstate=StringField('State*',validators=[DataRequired()])
	tpin=StringField('PIN*',validators=[DataRequired(),Length(min=6,max=6)])
	tephno=StringField('Emergency Phone No.*',validators=[DataRequired(),Length(min=10,max=10)])
	tmobile=StringField('Mobile*',validators=[DataRequired(),Length(min=10,max=10)])
	ttelphn=StringField('Telephone No.')	


	#Additional Information

	caste=RadioField('Caste[attach a copy of attested certificate]*', choices=[('gen','General'),('sc','S.C.'),('st','S.T.'),('obc','OBC'),('othr','Others')],validators=[DataRequired()])
	mtoungue=RadioField('Mother Tongue*', choices=[('ben','Bengali'),('hin','Hindi'),('eng','English'),('othr','Others')],validators=[DataRequired()])
	lang=StringField('Languages Known*',validators=[DataRequired(),Length(min=2,max=20)])

	#Health Information

	blgrp=StringField('Blood Group*',validators=[DataRequired(),Length(min=2,max=3)])
	teeth=IntegerField('Number of Teeth')
	height=StringField('Height*',validators=[DataRequired(),Length(min=2,max=10)])
	weight=StringField('Weight [Kg]*',validators=[DataRequired(),Length(min=2,max=3)])
	illness=StringField('Is your child suffering from any illness?',validators=[Length(min=2,max=20)])

	#Income

	famincome=RadioField('Family Income*', choices=[('1-','Less than 1 lac'),('3-','Upto 3 lacs'),('3+','More than 3 lacs')],validators=[DataRequired()])

	# More Info

	pschool=StringField('Previous School',validators=[Length(min=2,max=20)])
	classval= SelectField('Class*', choices=[('nur', 'Nursery'), ('lkg', 'LKG'), ('ukg', 'UKG'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')]) 
	reference=StringField('Reference',validators=[Length(min=2,max=20)])


	submit= SubmitField('Submit')


class ContactForm(FlaskForm):

	fname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "First Name"})
	lname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Last Name"})
	email = StringField('Email*',validators=[DataRequired()],render_kw={"placeholder": "Email"})
	phno = StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)],render_kw={"placeholder": "Phone No."})
	message= TextField('Message*',validators=[DataRequired()],render_kw={"placeholder": "Message"})
	submit= SubmitField('Submit your query')