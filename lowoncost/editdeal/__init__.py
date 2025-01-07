from flask import Blueprint

editdeal = Blueprint("editdeal", __name__, template_folder='templates')

from lowoncost.editdeal import handledeals