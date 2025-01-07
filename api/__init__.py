from flask import Blueprint

api = Blueprint("api", __name__, template_folder='templates')

from api import route
from api import auth
from api import deals