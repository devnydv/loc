from lowoncost import app
from flask import render_template, request, redirect, session, url_for
from lowoncost.editdeal.validate_edit import adddeal
from lowoncost.editdeal.editdealdb import addnewdeal, editdealdata, deletedeal
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
        correntprice = int(data["currentPrice"])
        originalprice = int(data["originalPrice"])
        data["status"] = False
        
        data["currentPrice"] = correntprice
        data["originalPrice"] = originalprice
        
        if "username" in session:
            username = session["username"]
            data["username"] = username
            
            addnewdeal(data)
            return redirect(url_for('dash', username=username))
        else:
            return redirect(url_for('login'))
        

@app.route('/profile/editdeal/<id>' , methods = ["GET", "POST"])
def editdeal(id):
    form = adddeal(request.form)
    if "username"in session:
        
        username = session["username"]
        if "data" in session:
            data = session["data"]
        else:
            alldata =  get_user_data(username)
            data = json.loads(alldata)
            data = data["data"]
        if request.method == "GET":
            items = data[0]['item_details']
            for item in items:
                if item['_id']['$oid'] == id:
                    form.description.data = item["description"]
                    mainitem = item
            return render_template("editdeal.html", form = form, item = mainitem, id= id)
    else:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        data = request.form
        data = dict(data)
        correntprice = int(data["currentPrice"])
        originalprice = int(data["originalPrice"])
        data["status"] = False
        data["username"] = username
        data["currentPrice"] = correntprice
        data["originalPrice"] = originalprice
        res = editdealdata(id, data)
        print(res)
        return redirect(url_for('dash', username=session["username"]))
    
@app.route('/details/')
def dealdetails():
    return render_template("dealdetail.html")


@app.route('/profile/delete/<id>')
def deletedeals(id):
    username = session["username"]
    deletedeal(id, username)
    return redirect(url_for('dash', username=username))
    