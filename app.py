from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define the form class
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

# Route to display and handle the form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Form data is valid and has been submitted
        name = form.name.data
        email = form.email.data
        message = form.message.data
        
        # Process form data (e.g., send email or save to database)
        return redirect(url_for('success'))
    
    return render_template('contact.html', form=form)

@app.route('/success')
def success():
    return 'Your message has been sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
