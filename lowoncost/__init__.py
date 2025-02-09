from flask import Flask

app = Flask(__name__)
app.secret_key ="doNotTryToSuck"

from lowoncost import route
from lowoncost.authfile import auth
from lowoncost.editdeal import editdeals
from lowoncost.admin.adminauth import adminlogin
from lowoncost.admin.admindash import admindash