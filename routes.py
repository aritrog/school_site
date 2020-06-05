from flask import render_template,url_for,flash, redirect,request 
from mainapp.forms import AdmissionForm
from mainapp.cruds import Admissiondb
from mainapp import app

@app.route('/')
def home():
	return """you have reached home"""


@app.route('/contact', methods=['GET','POST'])
def contact():
	form=ContactForm(request.form)
	if form.validate_on_submit():
		flash("Your message has been send to the authorities concern!")


@app.route('/admission', methods=['GET','POST'])
def admission():
	form=AdmissionForm(request.form)
	chc=form.validate_on_submit()
	print(chc)
	if chc:
		print("submited")
		flash(f"{form.name.data} have been registered in opur database","success")
		return redirect(url_for('home'))
	print(form.errors)	
	return render_template('admission.html', form=form)
