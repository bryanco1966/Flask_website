from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class SurveyForm(FlaskForm):
    party          = IntegerField('Party Indentification', validators=[DataRequired()])
    age            = IntegerField('How old are you?', validators=[DataRequired()])
    education      = IntegerField('What is your education level', validators=[DataRequired()])
    climate_change = IntegerField('Do you believe in Climate Change as a Man Made Phenomena', validators=[DataRequired()])
    submit         = SubmitField('Submit Survey')
