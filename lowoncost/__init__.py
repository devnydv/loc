from flask import Flask

app = Flask(__name__)
app.secret_key ="doNotTryToSuck"

from lowoncost import route
from lowoncost import auth