from flask import url_for,request,render_template,redirect,flash
from mainapp.cruds import Admissiondb
from mainapp.forms import AdmissionForm,ContactForm,NewsletterForm
from mainapp import app
@app.route('/')
def home():
	return render_template('index.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
	form=ContactForm(request.form)
	if form.validate_on_submit():

		flash("Your message has been send to the authorities concern!")
		return redirect(url_for('home'))
	return render_template('contact.html',form=form)	

@app.route('/about',methods=['GET','POST'])
def about():
	return render_template('about.html')

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

@app.route('/course',methods=['GET','POST'])
def course():
	return render_template('course.html')

@app.route('/blog',methods=['GET','POST'])
def blog():
	return render_template('blog.html')

@app.route('/teachers',methods=['GET','POST'])
def teachers():
	return render_template('teachers.html')

@app.route('/admission', methods=['GET','POST'])
def admission():
	form=AdmissionForm(request.form)
	if form.validate_on_submit():
		print(form.data.classval)
		user = Admissiondb(name=form.username.data,
						   email=form.email.data, 
						   phno=form.phno.data,
						   age=form.age.data,
						   classval=form.classval.data,
						   address=form.address.data
						)
		db.session.add(user)
		db.session.commit()
		flash(f"{form.name.data} have been registered in our database","success")
		return redirect(url_for('home'))
	print(form.errors)	
	return render_template('admission.html', form=form)
