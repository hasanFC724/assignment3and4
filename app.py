from flask import Flask, render_template, redirect, url_for
from forms import AssessmentForm  # Import the form class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for CSRF protectio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def home():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('information.html')

@app.route('/form', methods=['GET', 'POST'])
def contact():
    form = AssessmentForm()
    if form.validate_on_submit():
        # Process the form data, save it, send it, etc.
        return redirect(url_for('home'))  # Redirect to a different page after submit
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)