from flask import Blueprint

user = Blueprint("user", __name__, template_folder='templates')

from lowoncost.user import userdata