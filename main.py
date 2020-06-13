from mainapp import app
from flask_sqlalchemy import SQLAlchemy





# Run server
if __name__=="__main__":
	app.run(debug=True)