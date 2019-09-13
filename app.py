
from flask import Flask, render_template, request, flash
from my_portfolio.forms import ContactForm
from my_portfolio import app
from my_portfolio.models import db,Contact


#sendgrind import
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sendgrid_key = "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"

app.secret_key = 'development key'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mywork')
def mywork():
        return render_template('mywork.html')

@app.route('/passion')
def passion():
    return render_template('passion.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
        form = ContactForm()

        if request.method == "POST":
                message = Mail(
                        from_email=form.email.data,
                        to_emails="22pavolmedved@gmail.com",
                        subject='Welcome',
                        html_content='<strong>{}</strong> <strong> {} </strong> <strong> {} </strong>'.format(form.name.data,form.message.data,form.email.data))

                sg = SendGridAPIClient(sendgrid_key)
                response = sg.send(message) 
                print(response.status_code, response.body, response.headers) 

        return render_template('contact.html',form=form),200

        

@app.route('/send')
def send():
        return render_template('home.html')


@app.route('/creativity')
def creativity():
        return render_template('creativity.html')

@app.route('/baking')
def baking():
        return render_template('baking.html')

@app.route('/travel')
def travel():
        return render_template('travel.html')

@app.route('/sport')
def sport():
        return render_template('sport.html')




if __name__ == "__main__":
    app.run(debug=True)






