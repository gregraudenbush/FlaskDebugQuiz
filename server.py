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
        session['info'] = []
    else:
        for x in range(len(session['info'])):
            print x
            if session['info'][x] == "pizza":
                session['info'][x] = "pumkin pie"
    ##########################
    #Important!
    #Fix the above code.....
    # Session['info'] should display "pumkin pie" and NOT "pizza"
    #########################
    
    return render_template("index.html")


@app.route("/form", methods=['Post'])
def form():
    print session['info']
    
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    
    else:
        session['info'] = [str(request.form["FirstName"]), str(request.form['LastName']), str(request.form['FaveSnack'])]



    return redirect('/')



app.run(debug=True)