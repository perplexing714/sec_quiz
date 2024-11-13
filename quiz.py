import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_home():
    return render_template('home.html')
    
@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('render_home')) 
    
@app.route("/q1")
def render_ques1():
    return render_template('first.html')
    
@app.route("/q2", methods=['POST', 'GET'])
def render_ques2():
    if "answer1" not in session:
        session["answer1"]=request.form['answer1']
    return render_template('second.html')

@app.route("/q3", methods=['POST', 'GET'])
def render_ques3():
    if "answer2" not in session:
        session["answer2"]=request.form['answer2']
    return render_template('third.html')
    
@app.route("/q4", methods=['POST', 'GET'])
def render_ques4():
    if "answer3" not in session:
        session["answer3"]=request.form['answer3']
    return render_template('fourth.html')
    
@app.route("/q5", methods=['POST', 'GET'])
def render_ques5():
    if "answer4" not in session:
        session["answer4"]=request.form['answer4']
    return render_template('fifth.html')
    
@app.route("/results", methods=['POST', 'GET'])
def render_results():
    if "answer5" not in session:
        session["answer5"]=request.form['answer5']
    a=0
    if session["answer1"] == "option3":
        q1 = "correct"
        a = a + 1 
    else:
        q1 = "wrong"
        a = a
        
    if session["answer2"] == "2option2":
        q2 = "correct" 
        a = a + 1 
    else:
        q2 = "wrong"
        
    if session["answer3"] == "3option4":
        q3 = "correct" 
        a = a + 1 
    else:
        q3 = "wrong" 
        
    if session["answer4"] == "4option1":
        q4 = "correct"
        a = a + 1 
    else:
        q4 = "wrong"
        
    if session["answer5"] == "5option4":
        q5 = "correct" 
        a = a + 1 
    else:
        q5 = "wrong"
        
    return render_template('results.html', score=a, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    
if __name__=="__main__":
    app.run(debug=True)