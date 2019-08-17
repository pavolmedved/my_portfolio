from my_portfolio import app
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Email
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    message = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self,name,message,email):
        self.name = name
        self.message = message
        self.email =email

