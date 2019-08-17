
from flask import Flask, render_template, request, flash
from my_portfolio.forms import ContactForm
from my_portfolio import app
from my_portfolio.models import db,Contact


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/passion')
def passion():
    return render_template('passion.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
        form = ContactForm()
        name = form.name.data
        email = form.email.data
        message =  form.message.data
        contacting = Contact(name,email,message)
        print(name,email,message)
        db.session.add(contacting)
        db.session.commit()

        return render_template('contact.html',form=form)

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






