from flask import *
from flask_wtf import *
app = Flask(__name__)


@app.route("/")
def Show_Addresses():
    return render_template("home.html")

@app.route("/Add_Address")
def Add_Address():
    pass
@app.route("/Search_Address")
def Search_Address():
    pass

if __name__ == "__main__":
    app.run(debug=True)