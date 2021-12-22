from flask import Flask,render_template,request
import pickle
application=Flask(__name__)
@application.route('/')
def homepage():
    return render_template('index.html')
@application.route('/result',methods=['POST'])
def result():
    crime=request.form['CRIM']
    zone=request.form['ZN']
    indus=request.form['INDUS']
    charles=request.form['CHAS']
    nox=request.form['NOX']
    rm=request.form['RM']
    age=request.form['AGE']
    dis=request.form['DIS']
    rad=request.form['RAD']
    tax=request.form['TAX']
    ratio=request.form['PTR']
    black=request.form['BLACK']
    popstat=request.form['LSTAT']
    reg_mod=pickle.load(open('RandomForest.pickle','rb'))
    result=reg_mod.predict([[crime,zone,indus,charles,nox,rm,age,dis,rad,tax,ratio,black,popstat]])

    return 'The price of the house you are looking in boston area is:'+"$"+str(result)[1:-1]
   
if __name__=='__main__':
    application.run(debug=True)