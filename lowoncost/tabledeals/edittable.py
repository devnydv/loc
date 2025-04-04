from lowoncost import app
from flask import render_template, request, redirect, session, url_for
from lowoncost.tabledeals.tabledb import addtablerow, gettabledata, tableonedata, updatetable
@app.route("/dealtable", methods = ["GET", "POST"])
def table():
    #inser = addtablerow()
    data = gettabledata()
    if "username" in session:
        username = session["username"]
        return render_template("table.html", loggedin = True, userprofile = False, username = username, data = data)
    else:
        return render_template("table.html", loggedin = False, userprofile = False, data = data)
    

@app.route("/createtable", methods = ["GET", "POST"])

def createtable():
    if request.method == "POST":

        websites = request.form.get("website")
        
        
        # Splitting by '; ' to separate different platforms
        website_data = websites.split('; ')
        # Creating dictionary using dictionary comprehension
        website_dict = {w.split(', ')[0]: w.split(', ')[1] for w in website_data}
        data ={
            "name": request.form.get("name"),
            "price_range": "₹"+request.form.get("price_range"),
            "discount": request.form.get("discount")+"%",
            "category": request.form.get("category"),
            "rating": int(request.form.get("rating")),
            "website": website_dict,
        }
        addtablerow(data)
        return redirect(url_for("table"))
    data = gettabledata()
    return render_template("createtable.html", data = data)


@app.route("/edittable/<id>", methods = ["GET", "POST"])

def edittable(id):
    
    if request.method == "POST":
        
        websites = request.form.get("website")
        # Splitting by '; ' to separate different platforms
        website_data = websites.split('; ')
        # Creating dictionary using dictionary comprehension
        website_dict = {w.split(', ')[0]: w.split(', ')[1] for w in website_data}
        data ={
            "name": request.form.get("name"),
            "price_range": "₹"+request.form.get("price_range"),
            "discount": request.form.get("discount")+"%",
            "category": request.form.get("category"),
            "rating": int(request.form.get("rating")),
            "website": website_dict,
        }
        print(data)
        updatetable(data, id)
        return redirect(url_for("table"))
        
    data = tableonedata(id)
    
    return render_template("edittable.html", data = data)