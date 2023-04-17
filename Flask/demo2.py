from flask import Flask,render_template,request
import pickle
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/output',methods=['get','post'])
def prediction():
    Gen = request.form['gender']
    if Gen=='Male' or Gen=='male':
        Gen=1
    else:
        Gen=0
    Ms = request.form['married status']
    dep = int(request.form['dependents'])
    edu = request.form['education']
    if edu=='Graduate':
        edu=1
    else:
        Gen=0
    slemp = request.form['self employed']
    
    PA= request.form['property area']
    EAI = int(request.form['enter applicant income'])
    ELA= int(request.form['enter loan amount'])
    ELAT = int(request.form['enter loan amount term'])
    ECAI = int(request.form['enter co-applicant income'])

    inputvariables=[[Gen,Ms,dep,edu,slemp,PA,EAI,ELA,ELAT,ECAI]]
    model = pickle.load(open('Flask\loandt.pkl','rb'))
    pred=model.predict(inputvariables)


    if pred == 1:
        pred='LOAN WILL BE APPROVED'
    else:
        pred = 'LOAN WILL NOT BE APPROVED'
    return render_template("output.html",prediction=pred)


@app.route('/predict')
def outputpage():
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)