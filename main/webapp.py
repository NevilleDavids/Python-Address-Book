from flask import *
from flask_wtf import *
from io import StringIO
from Address import AddressOBJ
import pandas as pd
app = Flask(__name__)
app.secret_key = "OOOscecreet"
filepath = "C:/Users/E1002734/Desktop/Python Assessment Project/addresses.csv"
myaddresses = AddressOBJ.LoadAddresses(filepath)
@app.route("/")
def HomePage():
    return render_template("home.html")
@app.route("/Show_Addresses", methods = ["POST", "GET"])
def Show_Addresses():
    buff = StringIO()
    localadd = pd.DataFrame.from_dict(myaddresses)
    localadd.to_html(buff)
    html_string = buff.getvalue()

    file = open("C:/Users/E1002734/Desktop/Python Assessment Project/main/templates/addresses.html","w")
    file.write("<h1>Addresses</h1> {}".format(html_string))
    file.close()

    return render_template("addresses.html")

@app.route("/RenderAdd_Address", methods = ["POST", "GET"])
def RenderAdd_Address():
    return render_template("new.html")
@app.route("/AddA_Address", methods = ["POST", "GET"])
def AddA_Address():
    StreetNo = request.form.get("Street_No")
    StreetName = request.form.get("Street_Name")
    Surburb = request.form.get("Surburb")
    Province = request.form.get("Province")
    newaddress = AddressOBJ(int(StreetNo),StreetName,Surburb,Province)
    newaddress.AddAddress(myaddresses)
    newaddress.WriteToCSV(filepath,myaddresses)
    flash("Address Added")
    return render_template("home.html")
@app.route("/Search_Address", methods = ["POST", "GET"])
def Search_Address():
    return f"text for testing"


if __name__ == "__main__":
    app.run(debug=True)