from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, SubmitField
 
class ContactForm(FlaskForm):
  name = StringField("Name",  [validators.DataRequired()])
  email = StringField("Email",  [validators.DataRequired(), validators.Email()])
  message = TextAreaField("Message",  [validators.DataRequired()])
  submit = SubmitField("Send")