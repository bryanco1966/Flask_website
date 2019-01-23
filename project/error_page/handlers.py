#handlers.property
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

#create personalized error for Page not Found
# instead of using route method us app_errorhandler method to direct user
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

#create personalized error for forbidden actons
@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403
