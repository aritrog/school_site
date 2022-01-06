from datetime import datetime
import secrets
from PIL import Image
from flask import url_for,request,render_template,redirect,flash,send_file
from flask_mail import Mail, Message
from mainapp.cruds import Admissiondb, pdb
from mainapp.forms import AdmissionForm,ContactForm,NewsletterForm,SendMail,PostForm,GostForm
from mainapp import app
from mainapp import db
from mainapp import mail
from mainapp.pdfmaker import pdfgen
from .cruds import LogUser
from .cruds import MailRecords,Post,Gost
from flask_login import login_user, logout_user, login_required
from mainapp.picture_handler import image_handler
from werkzeug.security import generate_password_hash, check_password_hash
import os, uuid


##login and related shit lies here
@app.route('/login',methods=['GET','POST'])
def login():
	email = request.form.get('email')
	password = request.form.get('password')

	user = LogUser.query.filter_by(email=email).first()

	if not user or not check_password_hash(user.password,password):
		flash('Please check you credentials!')
		return render_template('index.html')

	login_user(user)
	return redirect(url_for('admin'))

@app.route('/signup', methods=['POST'])
def signup():
	email = request.form.get('email')
	name = request.form.get('name')
	mobile = request.form.get('mobile')
	password = request.form.get('password')
	user = LogUser.query.filter_by(email=email).first()
	if user:
		flash('Email address already exists')
		return redirect(url_for('home'))
	new_user = LogUser(email=email,  password=generate_password_hash(password, method='sha256'), mobile=mobile, name=name)
	db.session.add(new_user)
	db.session.commit()
	login_user(new_user)
	return redirect(url_for('admin'))
	
@app.route('/logout')
@login_required
def logout():
    logout_user() 
    return render_template('index.html')

#<-- DO NOT ENTER -->
##
@app.route('/admin',methods=['GET','POST'])
@login_required
def admin():
	form=SendMail(request.form)
	form2=PostForm(request.form)
	if form2.validate_on_submit():
			print('in validate')
			print(form2.pic.errors)
			f = request.files['pic']
			if f:
				print('uploading')
				random_hex = secrets.token_hex(8)
				_, f_ext = os.path.splitext(f.filename)
				namex = random_hex + f_ext
				pic_n = image_handler(f,namex,"posts")
				picn=pic_n
				data = {
					"_id": str(random_hex),
					"title": form2.title.data,
					"content": form2.content.data,
					"link":form2.link.data,
					"pic_name": picn,
					"date":datetime.now().strftime('%Y-%m-%d')
				}
				# post=Post(title=form2.title.data,content=form2.content.data,pic_name=picn)
			else:	
				data = {
					"_id": pdb.posts.count_documents({})+1,
					"title": form2.title.data,
					"content": form2.content.data,
					"link":form2.link.data,
					"date":datetime.now().strftime('%Y-%m-%d')
				}
			res = pdb.posts.insert_one(data)
			flash("Your post has been created")
			return redirect(url_for('home'))

	form3=GostForm(request.form)		
	return render_template('admin.html',form=form,form2=form2,form3=form3)


@app.route('/gpost',methods=['GET','POST'])
@login_required
def gpost():
	form=GostForm(request.form)
	if form.validate_on_submit:
		f = request.files['pic']
		if f:
			print('uploading')
			random_hex = secrets.token_hex(8)
			_, f_ext = os.path.splitext(f.filename)
			namex = random_hex + f_ext
			pic_n = image_handler(f,namex,"gallery")
			picn=pic_n
			data = {
			"_id": str(random_hex),
			"title": form.title.data,
			"pic_name": picn,
			"date":datetime.now().strftime('%Y-%m-%d')
			}
			res = pdb.gallery.insert_one(data)
			if not pdb.gtop.count_documents({"title":data["title"]}):
				res = pdb.gtop.insert_one(data)
			
	return redirect(url_for('gallery',title='all'))		


		




'''
from werkzeug.utils import secure_filename
@app.route('/edit',methods=['GET','POST'])
@login_required
def edit():
	if request.method == 'POST':
		image = Image.open(request.files['file'])
		i=request.form.get('spot')
		filename, extension = os.path.splitext(request.files['file'].filename)
		name='projectimage'+i
		image.save(r'/root/school_site/mainapp/static/images/%s.jpg' % name)
		return redirect(url_for('gallery',title='all'))
		# i=request.form.get('spot')
		# f = request.files['file']
		# filename, extension = os.path.splitext(f.filename)
		# #i='0'
		# if int(i)<10:
		# 	f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('projectimage'+'0'+i+extension)))
		# else:
		# 	f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('projectimage'+i+extension)))
		# flash('file uploaded successfully')
		# return redirect(url_for('gallery',title='all'))
'''		



@app.route('/blog',methods=['GET','POST'])
def blog():
	posts=pdb.posts.find({}).sort("$natural",-1)
	print("entered")
	print(posts)
	return render_template('blog.html', posts=posts)

@app.route('/sendmail', methods=['GET','POST'])
def sendmail():
	form=SendMail(request.form)
	if form.validate_on_submit():
		mails=MailRecords.query.all()
		msg = Message(form.sub.data, sender = 'apskanchraparawebsite@gmail.com')
		msg.html=render_template('mail.html',text=form.mess.data)
		for mail1 in mails:
			msg.add_recipient(mail1.email)
		mail.send(msg)
		flash("Your message has been send to the authorities concern!")
	return redirect(url_for('admin'))	
			

@app.route('/',methods=['GET','POST'])
def home():
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		email=form.email.data
		user = MailRecords.query.filter_by(email=email).first()
		print("printing mail records")
		print(MailRecords.query.all())
		if user:
			flash('Email address already exists')
			return render_template('index.html',form=form,show_form=show_form)

		new_email=MailRecords(email=email)
		db.session.add(new_email)
		db.session.commit()

		return render_template('index.html',form=form,show_form=show_form)
	print(form.errors)	
	return render_template('index.html',form=form,show_form=show_form)


@app.route('/contact', methods=['GET','POST'])
def contact():
	form=ContactForm(request.form)
	if form.validate_on_submit():
		print("hi query person")
		msg = Message('Hello hi', sender = 'apskanchraparawebsite@gmail.com', recipients = [form.email.data])
		msg.html = render_template('mail.html',text="Thank You for contacting Ambedkar Public School. We will come back to you as soon as possible.")
		mail.send(msg)
		flash("Your message has been send to the authorities concern!")
		return redirect(url_for('home'))
	return render_template('contact.html',form=form)	


@app.route('/get_logo')
def get_logo():
	return send_file('static/images/logo.png',mimetype='image/png')


@app.route('/gallery/<string:title>',methods=['GET','POST'])
def gallery(title="all"):
	
	show_form=True
	form=NewsletterForm(request.form)
	if form.validate_on_submit():
		show_form=False
		print("entered")
		return redirect(url_for('gallery',title='all'))
	print(form.errors)	
	if title == "all":
		gosts = pdb.gtop.find({})
		return render_template('gallery.html',form=form,show_form=show_form,gosts=gosts,show_title=True, title = "Gallery")
	else:
		gosts = pdb.gallery.find({"title":title})
		return render_template('gallery.html',form=form,show_form=show_form,gosts=gosts,show_title=False, title = title)


@app.route('/about',methods=['GET']) 
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

@app.route('/yoga')
def yoga():
	return render_template('yogapage.html')

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




@app.route("/post/<string:post_id>/delete", methods=['GET','POST'])
@login_required
def delete_post(post_id):
    res = pdb.posts.delete_one({"_id":post_id})
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('blog'))



@app.route("/gost/<string:gost_id>/<int:title>/delete", methods=['GET','POST'])
@login_required
def delete_gost(gost_id, title):
	if title:
		res = pdb.gtop.find_one({"_id":gost_id})
		title = res.get("title")
		res = pdb.gallery.delete_many({"title":title})
		res = pdb.gtop.delete_one({"_id":gost_id})
	res = pdb.gallery.delete_one({"_id":gost_id})
	flash('Your post has been deleted!', 'success')
	return redirect(url_for('gallery',title='all'))    
