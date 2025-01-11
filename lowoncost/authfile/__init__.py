from flask import Blueprint

authfile = Blueprint("authfile", __name__, template_folder='templates')

from lowoncost.authfile import auth