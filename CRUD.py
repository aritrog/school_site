from main import db


class Admissiondb(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100),nullable=False)
	email=db.Column(db.String(150))
	phno=db.Column(db.String(10),nullable=False)
	age=db.Column(db.Integer,nullable=False)
	classval=db.Column(db.String(10),nullable=False)
	address=db.Column(db.Text,nullable=False)
	date=db.Column(db.DateTime, default=datetime.utcnow)


	def __repr__(self):
		return f"user('{self.name}','{self.email}','{self.phno}','{self.age}','{self.classval}','{self.address}','{self.date}')"	
