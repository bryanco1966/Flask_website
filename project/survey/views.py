from flask import render_template, url_for, flash, request, redirect, Blueprint
from  flask_login import current_user, login_required
from project import db
from project.models import Survey
from project.survey.forms import SurveyForm

survey = Blueprint('survey', __name__)

@survey.route('/survey',methods=['GET','POST'])
@login_required
def complete_survey():
    form = SurveyForm()

    if form.validate_on_submit():

        survey = Survey(age            =form.age.data,
                        gender         =form.gender.data,
                        height         =form.height.data,
                        start_weight   =form.start_weight.data,
                        end_weight     =form.end_weight.data,
                        experience     =form.experience.data,
                        user_id        =current_user.id
                        )
        db.session.add(survey)
        db.session.commit()
        flash("Thanks for completing the survey")
        return redirect(url_for('core.index'))


    return render_template('survey.html',form=form)
