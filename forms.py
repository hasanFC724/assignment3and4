from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    name = StringField('Your Name:', validators=[DataRequired()])
    student_number = StringField('Student Number:', validators=[DataRequired()])
    email = StringField('Email Address:', validators=[DataRequired()])
    question1 = TextAreaField('Question 1: How satisfied are you with your academic progress at GIC?', validators=[DataRequired()])
    question2 = TextAreaField('Question 2: What areas do you think GIC can improve to support your academic success?', validators=[DataRequired()])
    grades = TextAreaField('Question 3: Grades Obtained in Courses:', validators=[DataRequired()])
    satisfaction = SelectField('Question 4: Overall Satisfaction with Academic Experience:', choices=[('','Select Satisfaction Level'), ('Excellent', 'Excellent'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], validators=[DataRequired()])
    suggestions = TextAreaField('Question 5: Suggestions for Improvement:', validators=[DataRequired()])
    submit = SubmitField('Submit')
