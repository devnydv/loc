from lowoncost import app
from api import api
from lowoncost.authfile import authfile
from lowoncost.editdeal import editdeal


# test file is ignores by git need correction before push

app.register_blueprint(api)
app.register_blueprint(authfile)
app.register_blueprint(editdeal)
if __name__=="__main__":
    app.run(debug=True)