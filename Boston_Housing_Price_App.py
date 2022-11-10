from flask import Flask
from flask import render_template,request
import pickle


app=Flask(__name__)
pickle_in= open('Boston_House_Prediction.pkl','rb')
reg=pickle.load(pickle_in)


@app.route('/', methods =["GET", "POST"])
def Boston_House_Price():
    if request.method == "POST":
        crim= float(request.form.get('CRIM'))
        zn  =float(request.form.get('ZN'))
        indus    =  float(request.form.get('INDUS'))
        chas   = float(request.form.get('CHAS'))
        nox    = float(request.form.get('NOX'))
        rm    = float(request.form.get('RM'))
        age     = float(request.form.get('AGE'))
        dis   = float(request.form.get('DIS'))
        rad    = float(request.form.get('RAD'))
        tax    = float(request.form.get('TAX'))
        ptratio      = float(request.form.get('PTRATIO'))
        b     = float(request.form.get('B'))
        lstat   = float(request.form.get('LSTAT'))
        prediction = reg.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]])
        return "The predicted value is "+ str(prediction)
    return render_template("Boston_House.html")

if __name__ == '__main__':
    app.run(host= "localhost",port="8000",debug=True)

