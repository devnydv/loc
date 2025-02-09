from flask import Blueprint

adminauth = Blueprint("adminauth", __name__, template_folder='templates', static_folder='static', static_url_path='/admin/adminauth/static')

from lowoncost.admin.adminauth import adminlogin