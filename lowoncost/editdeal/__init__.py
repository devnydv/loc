from flask import Blueprint

editdeal = Blueprint("editdeal", __name__, template_folder='templates', static_folder='static', static_url_path='/editdeal/static')

from lowoncost.editdeal import editdeals