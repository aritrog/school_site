from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

#init main
app=Flask(__name__)
app.config['SECRET_KEY']='edtgbaebaethetrshertsh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admission.db'
db=SQLAlchemy(app)


from mainapp import routes