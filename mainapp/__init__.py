
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail, Message
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

UPLOAD_FOLDER = '/home/dspace/Desktop/6thsem/school_site/mainapp/static/images'
#init main
app=Flask(__name__)
app.config['SECRET_KEY']='edtgbaebaethetrshertsh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admission.db'
app.config['SQLALCHEMY_BINDS']={'login': 'sqlite:///login.db',
								'newsletter' : 'sqlite:///newsletter.db',
								'posts': 'sqlite:///posts.db'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db=SQLAlchemy(app)
db.init_app(app)
#db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)



# from .cruds import LogUser
# class AdminModelView(ModelView):
#     def is_accessible(self):
#         return current_user.is_authenticated and not current_user.is_anonymous

# admin = Admin(app, name='coolapi', template_mode='bootstrap3')
# app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
# admin.add_view(AdminModelView(LogUser, db.session))




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