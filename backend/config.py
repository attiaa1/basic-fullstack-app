from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# init flask app

app = Flask(__name__)
CORS(app)

# init sqlite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODFICATIONS"] = False

# create instance of database => access to db through python app
db = SQLAlchemy(app)
