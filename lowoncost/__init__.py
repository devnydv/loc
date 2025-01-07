from flask import Flask

app = Flask(__name__)
app.secret_key ="doNotTryToSuck"

from lowoncost import route
from lowoncost.authfile import auth
from lowoncost.editdeal import handledeals