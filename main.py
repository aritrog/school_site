from flask import Flask,render_template,url_for,flash, redirect,request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from admissionform import AdmissionForm

#init main
app=Flask(__name__)
app.config['SECRET_KEY']='edtgbaebaethetrshertsh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admission.db'
db=SQLAlchemy(app)



@app.route('/')
def home():
	return """you have reached home"""

@app.route('/admission', methods=['GET','POST'])
def contact():
	form=AdmissionForm(request.form)
	chc=form.validate_on_submit()
	print(chc)
	if chc:
		print("submited")
		flash(f"{form.name.data} have been registered in opur database","success")
		return redirect(url_for('home'))
	print(form.errors)	
	return render_template('admission.html', form=form)








# Run server
if __name__=="__main__":
	app.run(debug=True)