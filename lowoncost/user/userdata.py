from lowoncost import app
from flask import render_template, redirect, session, url_for, request,flash
import json
from lowoncost.user.userdb import get_user_data, edit_user_data, get_cat_data
from lowoncost.user.validate_profile_edit import edit_profile



    
@app.route("/profile/<username>/", methods = ["GET", "POST"])
def dash(username):
    data = get_user_data(username)
    session['desc'] = data[0]["description"]
    print(data[0])
    if data == []:
        return redirect(url_for('error_404'))
    elif "username" in session and username == session['username']:
        # session['data'] = data
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : True, "items": items})
        #return  {"username":username, "logged in":True, "edit":True}
    elif "username" in session and username != session['username']:
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : False, "items": items})
    else:
       
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": False, 'userprofile' : False, "items": items})



@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    form =edit_profile(request.form) 
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            desc = session["desc"]
            name = session["username"]
            form.description.data = desc
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
    data = get_cat_data(username, cat)
    if data == []:
        return redirect(url_for('error_404'))
    elif "username" in session and username == session['username']:
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : True, "items": items} )
        #return  {"username":username, "logged in":True, "edit":True}
    elif "username" in session and username != session['username']:
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": True, 'userprofile' : False, "items": items} )
    else:
        items = data[0]["item_details"]
        return render_template("dash.html", userdata = data, navshow = {"loggedin": False, 'userprofile' : False, "items": items} )





@app.route('/profile/delete/<username>')
def deleteprofile(username):
    username = session["username"]
    #deleteuser(username)
    return redirect(url_for('sign'))