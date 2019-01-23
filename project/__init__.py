# This is my top level init file

# import in flask and create an instance

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

############################
######### DATABASE SETUP####
############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['AQLALCHEMY_TRACK_MONDIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)



######### END DATABASE SETUP ######


####################################
####### LOGIN CONFIGS##############
####################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

#### BRING IN BLUEPRINTS #########
from project.core.views import core
from project.users.views import users
from project.error_page.handlers import error_pages
from project.BlogPost.views import blog_posts
from project.survey.views import survey

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)
app.register_blueprint(survey)
