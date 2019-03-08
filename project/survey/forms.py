from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired

class SurveyForm(FlaskForm):
    age            = IntegerField('How old are you?', validators=[DataRequired()])
    gender         = IntegerField('What is your gender? Type 1 for Male and 2 for Female 3 for Other', validators=[DataRequired()])
    height         = IntegerField('How tall are you in inches?', validators=[DataRequired()])
    start_weight   = IntegerField('How much did you weigh in pounds at start of Whole 30?', validators=[DataRequired()])
    end_weight     = IntegerField('How much did you weigh in pounds at end of Whole 30?', validators=[DataRequired()])
    experience     = StringField('Please describe the Whole 30 exeperience for you.', validators=[DataRequired()])
    submit         = SubmitField('Submit Survey')
