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
        # Constructing a string with the form responses
        responses = f"Name: {form.name.data}\n" \
                    f"Student Number: {form.student_number.data}\n" \
                    f"Email: {form.email.data}\n" \
                    f"Question 1 Response: {form.question1.data}\n" \
                    f"Question 2 Response: {form.question2.data}\n" \
                    f"Grades: {form.grades.data}\n" \
                    f"Satisfaction: {form.satisfaction.data}\n" \
                    f"Suggestions: {form.suggestions.data}\n"

        # Name of the file to save the responses
        filename = "form_submissions.txt"

        # Open the file in append mode and write the responses
        with open(filename, "a") as file:
            file.write(responses + "\n---\n")  # Separate submissions with ---

        return redirect(url_for('home'))  # Redirect after POST
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)