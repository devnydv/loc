from flask import Blueprint

tabledeal = Blueprint("tabledeal", __name__, template_folder='templates', static_folder='static', static_url_path='/editdeal/static')

from lowoncost.tabledeals import edittable