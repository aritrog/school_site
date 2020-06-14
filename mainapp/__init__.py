 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail, Message

#init main
app=Flask(__name__)
app.config['SECRET_KEY']='edtgbaebaethetrshertsh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admission.db'
app.config['SQLALCHEMY_BINDS']={'login': 'sqlite:///login.db'}

db=SQLAlchemy(app)
db.init_app(app)
#db.create_all()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'apskanchraparawebsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'apskanchrapara@2020'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


from mainapp import routes