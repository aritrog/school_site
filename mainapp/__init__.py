 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail, Message
from flask_login import LoginManager

#init main
app=Flask(__name__)
app.config['SECRET_KEY']='edtgbaebaethetrshertsh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admission.db'
app.config['SQLALCHEMY_BINDS']={'login': 'sqlite:///login.db'
								'newsletter' : 'sqlite:///newsletter.db'}

db=SQLAlchemy(app)
db.init_app(app)
#db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .cruds import LogUser
@login_manager.user_loader
def load_user(user_id):
	return LogUser.query.get(int(user_id))

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'apskanchraparawebsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'apskanchrapara@2020'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


from mainapp import routes