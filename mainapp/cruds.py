from datetime import datetime
from flask_login import UserMixin
from . import db


class Admissiondb(db.Model):
	pid = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100),nullable=False)
	email=db.Column(db.String(150),nullable=False)
	dob=db.Column(db.DateTime, nullable=False)
	gender=db.Column(db.String(6),nullable=False)
	nationality=db.Column(db.String(6),nullable=False)

	fathername=db.Column(db.String(25),nullable=False)
	fage = db.Column(db.Integer,nullable=False)
	fedu=db.Column(db.String(6),nullable=False)
	fincome = db.Column(db.Integer,nullable=False)
	fphno=db.Column(db.String(6),nullable=False)

	mothername=db.Column(db.String(25),nullable=False)
	mage = db.Column(db.Integer,nullable=False)
	medu=db.Column(db.String(6),nullable=False)
	mincome = db.Column(db.Integer,nullable=False)
	mphno=db.Column(db.String(6),nullable=False)

	guardianname=db.Column(db.String(20),nullable=False)
	gage = db.Column(db.Integer,nullable=False)
	gedu=db.Column(db.String(6),nullable=False)
	gincome = db.Column(db.Integer,nullable=False)
	gphno=db.Column(db.String(6),nullable=False)

	hldno=db.Column(db.String(40),nullable=False)
	city=db.Column(db.String(20),nullable=False)
	dist=db.Column(db.String(20),nullable=False)
	state=db.Column(db.String(20),nullable=False)
	pin=db.Column(db.String(6),nullable=False)

	thldno=db.Column(db.String(40),nullable=False)
	tcity=db.Column(db.String(20),nullable=False)
	tdist=db.Column(db.String(20),nullable=False)
	tstate=db.Column(db.String(20),nullable=False)
	tpin=db.Column(db.String(6),nullable=False)

	ephno=db.Column(db.String(6),nullable=False)
	mobile=db.Column(db.String(6),nullable=False)
	telphn=db.Column(db.String(6),nullable=False)

	caste=db.Column(db.String(10),nullable=False)
	mtoungue=db.Column(db.String(10),nullable=False)
	lang=db.Column(db.String(30),nullable=False)

	blgrp=db.Column(db.String(6),nullable=False)
	teeth=db.Column(db.Integer,nullable=False)
	height=db.Column(db.String(6),nullable=False)
	weight=db.Column(db.String(6),nullable=False)
	illness=db.Column(db.String(30),nullable=False)

	famincome=db.Column(db.Integer,nullable=False)

	pschool=db.Column(db.String(20),nullable=False)
	reference=db.Column(db.String(30),nullable=False)
	classval=db.Column(db.String(7),nullable=False)
	xdoc=db.Column(db.String(40),nullable=False)
	odoc=db.Column(db.String(40),nullable=False)
	subj=db.Column(db.String(70),nullable=False)
	coa=db.Column(db.String(20),nullable=False)

	
	date=db.Column(db.DateTime, default=datetime.utcnow)


	def __repr__(self):
		return f"user('{self.name}','{self.email}','{self.phno}','{self.age}','{self.classval}','{self.address}','{self.date}')"	

class LogUser(UserMixin, db.Model):
	__bind_key__ = 'login'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100),nullable=False)
	mobile = db.Column(db.String(10),nullable=False)
	name = db.Column(db.String(1000),nullable=False)