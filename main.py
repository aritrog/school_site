from mainapp import app

#init main
app=Flask(__name__)
app.config['SECRET_KEY']='edtgbaebaethetrshertsh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admission.db'
db=SQLAlchemy(app)



# Run server
if __name__=="__main__":
	app.run(debug=True)