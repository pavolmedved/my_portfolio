from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))


basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SECRET_KEY'] = "[pavol loves organic strawberry fruits]"