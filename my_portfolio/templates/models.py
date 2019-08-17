from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), primary_key=True, unique=True)
    phone_number = db.Column(db.Integer)
    address = db.Column(db.String(150))
    email_address = db.Column(db.String(100))
