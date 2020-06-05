from flask import url_for,request,render_template,redirect,flash
from mainapp.cruds import Admissiondb
from mainapp.forms import AdmissionForm
from mainapp import app
@app.route('/')
def home():
	return render_template('index.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
	form=ContactForm(request.form)
	if form.validate_on_submit():
		flash("Your message has been send to the authorities concern!")

@app.route('/about',methods=['GET','POST'])
def about():
	return render_template('about.html')

@app.route('/home',methods=['GET','POST'])
def about():
	return render_template('index.html')

@app.route('/course',methods=['GET','POST'])
def about():
	return render_template('course.html')

@app.route('/blog',methods=['GET','POST'])
def about():
	return render_template('blog.html')

@app.route('/contact',methods=['GET','POST'])
def about():
	return render_template('contact.html')

@app.route('/admission', methods=['GET','POST'])
def admission():
	form=AdmissionForm(request.form)
	chc=form.validate_on_submit()
	print(chc)
	if chc:
		print("submitted")
		flash(f"{form.name.data} have been registered in opur database","success")
		return redirect(url_for('home'))
	print(form.errors)	
	return render_template('admission.html', form=form)
