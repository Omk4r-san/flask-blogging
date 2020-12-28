from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_debug import Debug
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '01ca564fac9185a04f417ae3211ba8f6'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes