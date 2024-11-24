from flask import render_template, request
from api import api


# other user routes

@api.route("/api")
def apihome():
    return {"msg":"this is home page for the api. Do not missuse this end point."}


    

    

