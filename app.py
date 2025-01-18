from lowoncost import app

from lowoncost.authfile import authfile
from lowoncost.editdeal import editdeal
from lowoncost.user import user


app.register_blueprint(authfile)
app.register_blueprint(editdeal)
app.register_blueprint(user)


if __name__=="__main__":
    app.run(debug=True)