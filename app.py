from lowoncost import app
from api import api


# test file is ignores by git need correction before push

app.register_blueprint(api)

if __name__=="__main__":
    app.run(debug=True)