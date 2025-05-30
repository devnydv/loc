from lowoncost import app
from flask import render_template, request, redirect, session, url_for
from lowoncost.editdeal.validate_edit import adddeal
from lowoncost.editdeal.editdealdb import addnewdeal, editdealdata, deletedeal, getaitem, recomand
from lowoncost.user.userdb import get_user_data
import json



@app.route("/profile/addnewdeal", methods = ["GET", "POST"])
def newdeal():
    form = adddeal(request.form)
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            return render_template("adddeal.html", form = form, name= username)
        else:
            return redirect(url_for('login'))
    if request.method == "POST":
        data = request.form
        data = dict(data)
        # pros = data["pros"].split(';')
        # pros = [item.strip() for item in pros]
        # cons = data["cons"].split(';')
        # cons = [item.strip() for item in cons]
        #data["pros"] = pros
        #data["cons"] = cons
        correntprice = int(data["currentPrice"])
        originalprice = int(data["originalPrice"])

        data["status"] = "pending"
        data["currentPrice"] = correntprice
        data["originalPrice"] = originalprice
        
        if "username" in session:
            username = session["username"]
            data["username"] = username
            
            addnewdeal(data)
            return redirect(url_for('dash', name=username))
        else:
            return redirect(url_for('login'))
        

@app.route('/profile/editdeal/<id>' , methods = ["GET", "POST"])
def editdeal(id):
    form = adddeal(request.form)
    if "username"in session:
        
        username = session["username"]
        
        data = getaitem(id)
        #print(data)
        if request.method == "GET":
            item = data
            form.description.data = item["description"]
            mainitem = item
            return render_template("editdeal.html", form = form, item = mainitem, id= id)
    else:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        data = request.form
        data = dict(data)
        # pros = data["pros"].split(';')
        # pros = [item.strip() for item in pros]
        # cons = data["cons"].split(';')
        # cons = [item.strip() for item in cons]
        # data["pros"] = pros
        # data["cons"] = cons
        correntprice = int(data["currentPrice"])
        originalprice = int(data["originalPrice"])
        data["status"] = "pending"
        data["username"] = username
        data["currentPrice"] = correntprice
        data["originalPrice"] = originalprice
        
        res = editdealdata(id, data)
        return redirect(url_for('dash', name=session["username"]))
    
@app.route('/details/<id>')
def dealdetails(id):
    data = getaitem(id)
    recomandation = recomand()
    recomandation = [item for item in recomandation if item["_id"]['$oid'] != id]

    
    if data == None:
        return redirect(url_for('error_404'))
    if "username" in session:
        username = session["username"]
        return render_template("dealdetail.html", loggedin = True, userprofile = False, username = username, data = data, recomand= recomandation)
    else:
        return render_template("dealdetail.html", loggedin = False, userprofile = False, data= data, recomand= recomandation)



@app.route('/api/delete/<id>')
def deletedeals(id):
    if "username" in session:
        username = session["username"]
        deletedeal(id, username)
        return redirect(url_for('dash', name=username))
    else:
        return redirect(url_for('login'))
    