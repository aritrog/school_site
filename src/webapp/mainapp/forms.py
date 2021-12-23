from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField,TextAreaField,DateField,RadioField,BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed

class AdmissionForm(FlaskForm):
	
	#Student Info
	name = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email*')
	dob = DateField('Date of Birth*', validators=[DataRequired()], format='%Y-%m-%d')
	gender=RadioField('Gender*', choices=[('m','Male'),('fm','Female'),('othr','Others')],validators=[DataRequired()])
	nationality=RadioField('Nationality*', choices=[('indian','Indian'),('nri','NRI')],validators=[DataRequired()])

	#parental Info

	fathername = StringField('Father Name*',validators=[Length(min=2,max=20)])
	fage= IntegerField("Age*",validators=[])
	fedu = StringField('Education*',validators=[Length(min=2,max=10)])
	fincome= IntegerField('Annual Income*',validators=[])
	fphno= StringField('Phone no*',validators=[Length(min=10,max=10)])
	
	mothername = StringField('Mother Name*',validators=[Length(min=2,max=20)])
	mage= IntegerField("Age*",validators=[])
	medu = StringField('Education*',validators=[Length(min=2,max=10)])
	mincome= IntegerField('Annual Income*',validators=[])
	mphno= StringField('Phone no*',validators=[Length(min=10,max=10)])
	
	guardianname = StringField('Guardian Name*',validators=[Length(min=2,max=20)])
	gage= IntegerField("Age*",validators=[])
	gedu = StringField('Education*',validators=[Length(min=2,max=10)])
	gincome= IntegerField('Annual Income*',validators=[])
	gphno= StringField('Phone no*',validators=[Length(min=10,max=10)])


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
	chck=BooleanField(' Same as Permanent Address',default=False)
	thldno=StringField('Holding No. / Quarters No. *')
	tcity=StringField('City*')
	tdist=StringField('District*')
	tstate=StringField('State*')
	tpin=StringField('PIN*',validators=[Length(min=6,max=6)])


	#Additional Information

	caste=RadioField('Caste [ attach a copy of attested certificate ]*', choices=[('gen','General'),('sc','S.C.'),('st','S.T.'),('obc','OBC'),('othr','Others')],validators=[DataRequired()])
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
	xdoc=StringField('Xerox Copies of')
	odoc=StringField('Original copies of')
	subj=StringField('Subjects opted for *', validators=[DataRequired()])
	coa=StringField('Wether applied for change of Date of Birth/ Address ?')


	#uploads

	document = FileField('Document', validators=[ FileAllowed(['pdf', 'jpg','png'], 'Image or PDF only!')])
	profile = FileField('Profile', validators=[ FileAllowed(['jpg', 'png'], 'Images only!')])

	#submit
	dec='DECLARE'
	acc='ACCEPT'
	declare=StringField("",validators=[DataRequired()])
	accept=StringField("",validators=[DataRequired()])
	submit= SubmitField('Submit')


class ContactForm(FlaskForm):

	fname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "First Name"})
	lname = StringField('Name*',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Last Name"})
	email = StringField('Email*',validators=[DataRequired()],render_kw={"placeholder": "Email"})
	phno = StringField('Phone no*',validators=[DataRequired(),Length(min=10,max=10)],render_kw={"placeholder": "Phone No."})
	message= TextAreaField('Message*',validators=[DataRequired()],render_kw={"placeholder": "Message"})
	submit= SubmitField('Submit your query')

class NewsletterForm(FlaskForm):
	email = StringField('Email*',validators=[DataRequired()],render_kw={"placeholder": "Email"})
	submit= SubmitField('Subscribe')

class SendMail(FlaskForm):
	sub=StringField('Subjects*',validators=[DataRequired()],render_kw={"placeholder": "Email Subject"})
	mess=TextAreaField('Message*',validators=[DataRequired()],render_kw={"placeholder": "Message"})
	submit= SubmitField('Subscribe')

class PostForm(FlaskForm):
	title=StringField('Title',validators=[DataRequired()])
	content=TextAreaField('Content',validators=[DataRequired()])
	pic=FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit=SubmitField('Post')

class GostForm(FlaskForm):
	pic=FileField('Picture', validators=[FileAllowed(['jpg', 'png']),DataRequired()])
	submit=SubmitField('Post')		
