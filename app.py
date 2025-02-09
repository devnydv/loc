from lowoncost import app

from lowoncost.authfile import authfile
from lowoncost.editdeal import editdeal
from lowoncost.user import user
from lowoncost.admin.adminauth import adminauth
from lowoncost.admin.admindash import admindash

app.register_blueprint(authfile)
app.register_blueprint(editdeal)
app.register_blueprint(user)
app.register_blueprint(adminauth)
app.register_blueprint(admindash)


if __name__=="__main__":
    app.run(debug=True)