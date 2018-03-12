from flask import Flask, request, redirect, session, flash, render_template
import sys

app = Flask(__name__)
app.secret_key = "unicorns"

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!
####################

@app.route('/') 
def index(): 
    
    if 'info' not in session:
        session['info'] = ""
    else:
        flash("pumkin pie")
        session['info'] = "pumkin pie"
        print session['info']
        # for x in session['info']:
        #     print x
        #     if x == "pizza":
        #         flash("pumkin pie") 
        
    ##########################
    #Important!
    #Fix the above code.....
    # Session['info'] should display "pumkin pie" and NOT "pizza"
    #########################
    sys.stdout.flush()  # to flush output
    return render_template("index.html")

@app.route("/form", methods=['POST'])
def myform():
    print session['info']
    if (len(request.form['FirstName'])) < 1 or (len(request.form['Last_Name'])) < 1:
        flash("Please Complete Form")
    else:
        # print session['info']
        session['info'] = [request.form["FirstName"], request.form['LastName'], request.form['FaveSnack']]

    sys.stdout.flush()  # to flush output
    return redirect('/')

app.run(debug=True)