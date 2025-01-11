from lowoncost import app
from flask import render_template, redirect, session, url_for, request
import json
from lowoncost.user.userdb import get_user_data, edit_user_data
from lowoncost.user.validate_profile_edit import edit_profile


@app.route("/profile/<username>", methods = ["GET", "POST"])
def dash(username):
    data = get_user_data(username)
    
    if data == []:
        return redirect(url_for('error_404'))
    elif "username" in session and username == session['username']:
        data = json.loads(data)
        data = data["data"]
        session['data'] = data
        return render_template("dash.html", userdata = data, loggedin = True, edit = True, userprofile = True)
        #return  {"username":username, "logged in":True, "edit":True}
    elif "username" in session and username != session['username']:
        data = json.loads(data)
        data = data["data"]
        return render_template("dash.html", userdata = data, loggedin = True, edit = False, userprofile = False)
    else:
        data = json.loads(data)
        data = data["data"]
        return render_template("dash.html", userdata = data, loggedin = False, edit = False, userprofile =False)
    




@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    form =edit_profile(request.form) 
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            data = session["data"]
            name = session["username"]
            form.description.data = data[0]['description']
            
            return render_template("editprofile.html", name= name , form = form)
    if request.method == "POST":
        return "POST"
    else:
        return redirect(url_for('error_404'))