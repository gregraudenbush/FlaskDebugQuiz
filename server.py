from flask import Flask, request, render_template, redirect, session, flash
app = Flask(__name__)
app.secret_key = "unicorns"

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!
####################

@app.route('/') 
def index(): 
    
    if "info" not in session:
        session['info'] = ""
    
    return render_template("index.html", info = session['info'])


@app.route('/form', methods=['POST'])
def form():
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = [str(request.form['FirstName']), str(request.form['LastName']), str(request.form['FaveSnack'])]
        for x in session['info']:
            if x == "pizza":
                x = "pumpkin pie"
                session['info'].pop()
                session['info'].append(x)
        
    return redirect('/')

app.run(debug=True)