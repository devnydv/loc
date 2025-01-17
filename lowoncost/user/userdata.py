from lowoncost import app
from flask import render_template, redirect, session, url_for, request,flash
import json
from lowoncost.user.userdb import get_user_data, edit_user_data
from lowoncost.user.validate_profile_edit import edit_profile


@app.route("/profile/<username>/", methods = ["GET", "POST"])
def dash(username):
    data = get_user_data(username)
    if data == []:
        return redirect(url_for('error_404'))
    elif "username" in session and username == session['username']:
        data = json.loads(data)
        data = data["data"]
        items = data[0]["item_details"]
        session['data'] = data
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : True, "items": items})
        #return  {"username":username, "logged in":True, "edit":True}
    elif "username" in session and username != session['username']:
        data = json.loads(data)
        data = data["data"]
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : False, "items": items})
    else:
        data = json.loads(data)
        data = data["data"]
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": False, 'userprofile' : False, "items": items})
    




@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    form =edit_profile(request.form) 
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            data = session["data"]
            name = session["username"]
            form.description.data = data[0]['description']
            return render_template("editprofile.html", name= name , form = form, username = username)
    if request.method == "POST":
        data = dict(request.form)
        name = session["username"]
        # changing username is disabled
        #just remove the below line and disabled from the template input to make it working
        data['username'] = name
        
        res = edit_user_data(name, data)
        
        if res == True:
            session["username"] = data["username"]
            return redirect(url_for('dash', username = session["username"]))
        flash(res["msg"])
        name = session["username"]
        return render_template("editprofile.html", name= name , form = form)
    else:
        return redirect(url_for('error_404'))
    
def filter(items, cat ):
    filterd_items = []
    for item in items:
        if item["category"] == cat:
            filterd_items.append(item)
    return filterd_items

@app.route("/profile/<username>/<cat>", methods = ["GET", "POST"])
def dash_cate(username,cat):
    if "data" not in session:
        data = get_user_data(username)
        data = json.loads(data)
        data = data["data"]
    else:
        data = session["data"]
    if data == []:
        return redirect(url_for('error_404'))
    elif "username" in session and username == session['username']:
        items = data[0]["item_details"]
        filterd_items  = filter(items, cat)
        session['data'] = data
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : True, "items": filterd_items} )
        #return  {"username":username, "logged in":True, "edit":True}
    elif "username" in session and username != session['username']:
        items = data[0]["item_details"]
        filterd_items  = filter(items, cat)
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : False, "items": filterd_items} )
    else:
        items = data[0]["item_details"]
        filterd_items  = filter(items, cat)
        return render_template("dash.html", userdata = data, navshow = {"loggedin": False, 'userprofile' : False, "items": filterd_items} )







@app.route('/profile/delete/<username>')
def deleteprofile(username):
    username = session["username"]
    #deleteuser(username)
    return redirect(url_for('sign'))