from flask import url_for,request,render_template,redirect,flash
from flask_mail import Mail, Message
from mainapp.cruds import Admissiondb
from mainapp.forms import AdmissionForm,ContactForm,NewsletterForm
from mainapp import app
from mainapp import db
from mainapp import mail
from mainapp.pdfmaker import pdfgen


@app.route('/',methods=['GET','POST'])
def home():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return render_template('index.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('index.html',form=form,show_form=show_form)


@app.route('/contact', methods=['GET','POST'])
def contact():
	form=ContactForm(request.form)
	if form.validate_on_submit():
		print("hi bby")
		msg = Message('Hello hi', sender = 'apskanchraparawebsite@gmail.com', recipients = [form.email.data])
		msg.body = """
					<!DOCTYPE html>
					<html>
						<head>
							<title>Hi</title>
						</head>
						<body>
							<div>
								<h1>AMBEDKAR PUBLIC SCHOOL</h1>
								<p>
									Thank You for reaching out to us
									<br>
								   	We will be contact you with more information soon.
									<br>
									Regards,
									<br>
									Team APS.
								</p>
							</div>
						</body>
					</html>
				   """		
		mail.send(msg)
		flash("Your message has been send to the authorities concern!")
		return redirect(url_for('home'))
	return render_template('contact.html',form=form)	


@app.route('/gallery',methods=['GET','POST'])
def gallery():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return render_template('gallery.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('gallery.html',form=form,show_form=show_form)

@app.route('/about',methods=['GET','POST'])
def about():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return render_template('about.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('about.html',form=form,show_form=show_form)

@app.route('/course',methods=['GET','POST'])
def course():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return render_template('course.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('course.html',form=form,show_form=show_form)

@app.route('/blog',methods=['GET','POST'])
def blog():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return render_template('blog.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('blog.html',form=form,show_form=show_form)

@app.route('/teachers',methods=['GET','POST'])
def teachers():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return render_template('teachers.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('teachers.html',form=form,show_form=show_form)

@app.route('/admission', methods=['GET','POST'])
def admission():
	pdf=pdfgen()
	form=AdmissionForm(request.form)
	if form.validate_on_submit():
		print(form)
		if form.chck.data :
			user = Admissiondb(name=form.name.data,
							   email=form.email.data, 
							   dob=form.dob.data,
							   gender=form.gender.data,
							   nationality=form.nationality.data,
							   
							   fathername =form.fathername.data,
							   fage=form.fage.data,
							   fedu=form.fedu.data,
							   fincome=form.fincome.data,
							   fphno=form.fphno.data,

							   mothername =form.mothername.data,
							   mage=form.mage.data,
							   medu=form.medu.data,
							   mincome=form.mincome.data,
							   mphno=form.mphno.data,

							   guardianname =form.guardianname.data,
							   gage=form.gage.data,
							   gedu=form.gedu.data,
							   gincome=form.gincome.data,
							   gphno=form.gphno.data,

							   hldno=form.hldno.data,
							   city=form.city.data,
							   dist=form.dist.data,
							   state=form.state.data,
							   pin=form.pin.data,
							   ephno=form.ephno.data,
							   mobile=form.mobile.data,
							   telphn=form.telphn.data,

							   thldno=form.hldno.data,
							   tcity=form.city.data,
							   tdist=form.dist.data,
							   tstate=form.state.data,
							   tpin=form.pin.data,

							   caste=form.caste.data,
							   mtoungue=form.mtoungue.data,
							   lang=form.lang.data,

							   blgrp=form.blgrp.data,
							   teeth=form.teeth.data,
							   height=form.height.data,
							   weight=form.weight.data,
							   illness=form.illness.data,

							   famincome=form.famincome.data,

							   pschool=form.pschool.data,
							   classval=form.classval.data,
							   reference=form.reference.data,
							   xdoc=form.xdoc.data,
							   odoc=form.odoc.data,
							   subj=form.subj.data,
							   coa=form.coa.data,

							)

		else: 	
			user = Admissiondb(name=form.name.data,
							   email=form.email.data, 
							   dob=form.dob.data,
							   gender=form.gender.data,
							   nationality=form.nationality.data,
							   
							   fathername =form.fathername.data,
							   fage=form.fage.data,
							   fedu=form.fedu.data,
							   fincome=form.fincome.data,
							   fphno=form.fphno.data,

							   mothername =form.mothername.data,
							   mage=form.mage.data,
							   medu=form.medu.data,
							   mincome=form.mincome.data,
							   mphno=form.mphno.data,

							   guardianname =form.guardianname.data,
							   gage=form.gage.data,
							   gedu=form.gedu.data,
							   gincome=form.gincome.data,
							   gphno=form.gphno.data,

							   hldno=form.hldno.data,
							   city=form.city.data,
							   dist=form.dist.data,
							   state=form.state.data,
							   pin=form.pin.data,
							   ephno=form.ephno.data,
							   mobile=form.mobile.data,
							   telphn=form.telphn.data,

							   thldno=form.thldno.data,
							   tcity=form.tcity.data,
							   tdist=form.tdist.data,
							   tstate=form.tstate.data,
							   tpin=form.tpin.data,

							   caste=form.caste.data,
							   mtoungue=form.mtoungue.data,
							   lang=form.lang.data,

							   blgrp=form.blgrp.data,
							   teeth=form.teeth.data,
							   height=form.height.data,
							   weight=form.weight.data,
							   illness=form.illness.data,

							   famincome=form.famincome.data,

							   pschool=form.pschool.data,
							   classval=form.classval.data,
							   reference=form.reference.data,
							   xdoc=form.xdoc.data,
							   odoc=form.odoc.data,
							   subj=form.subj.data,
							   coa=form.coa.data,

							)
		db.session.add(user)
		db.session.commit()
		flash(f"{form.name.data} have been registered in our database","success")
		return redirect(url_for('home'))
	print(form.errors)	
	return render_template('admission.html', form=form)
