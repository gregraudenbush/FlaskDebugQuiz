from flask import Flask, request, redirect, session, flash, render_template
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
        session['info'] = "pumpkin pie"
    else:
        for x in range (0, len(session['info'])):
            # print x
            if session['info'][x] == "pizza":
                # print 'true'
                session['info'][x] = "pumpkin pie"
                # print x
                # print session['info']
    # session['info'] = 'pumpkin pie'
    # print session['info']
    ##########################
    #Important!
    #Fix the above code.....
    # Session['info'] should display "pumkin pie" and NOT "pizza"
    #########################
    
    return render_template("index.html", info = session['info'])


@app.route('/form', methods=['POST'])
def submit_form():
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = [request.form["FirstName"], request.form['LastName'], request.form['FaveSnack']]
    return redirect('/')

app.run(debug=True)