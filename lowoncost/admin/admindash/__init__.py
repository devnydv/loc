from flask import Blueprint

admindash = Blueprint("admindash", __name__, template_folder='templates', static_folder='static', static_url_path='/admin/admindash/static')

from lowoncost.admin.admindash import dash