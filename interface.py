from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import Boston
app = Flask(__name__)

########################################################################

@app.route('/') 
def hello_flask():
    print("Welcome to Flask")
    # return render_template("home.html")
    return 'Hello Python'

#########################################################################


@app.route('/predict')
def get_predicted():

    data = request.get_json()
    CRIM = eval(data['CRIM'])
    ZN = eval(data['ZN'])
    INDUS = eval(data['INDUS'])
    CHAS = eval(data['CHAS'])
    NOX = eval(data['NOX'])
    RM = eval(data['RM'])
    AGE = eval(data['AGE'])
    DIS = eval(data['DIS'])
    RAD = eval(data['RAD'])
    TAX = eval(data['TAX'])
    PTRATIO = eval(data['PTRATIO'])
    B = eval(data['B'])
    LSTAT = eval(data['LSTAT'])
    
    print("CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT",CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT)
    boston = Boston(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT)
    boston = boston.get_predicted()
                    
    return jsonify({"Result":f"Predicted Boston Price are : {boston}"})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)