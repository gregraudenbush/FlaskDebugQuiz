from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/') 
def index(): 
    if "info" not in session:
        session['info'] = "pumpkin pie"
   
    print session['info']
    return render_template("index.html", info = session['info'])

@app.route("/form", methods=['POST'])
def form():
    
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = [str(request.form["FirstName"]), str(request.form['LastName']), str(request.form['FaveSnack'])]
        print request.form['FirstName']

    return redirect('/')



app.run(debug=True)