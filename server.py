from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "unicorns"

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!
####################

@app.route('/') 
def index(): 
    if "info" in session:
        print session['info']
        if session['info'] == "pizza":
            session['info'] = "pumkin pie"
    ##########################
    #Important!
    #Fix the above code.....
    # Session['info'] should display "pumkin pie" and NOT "pizza"
    #########################
    
    return render_template("index.html", info = session['info'])


@app.route("/form", methods=["POST"])
def form():
    # print request.form['FaveSnack']
    # print request.form['FirstName']
    # print request.form['LastName']
    # print len(request.form['FirstName'])
    # print len(request.form['LastName'])
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("please fillout form")
    else:
        session['info'] = request.form['FaveSnack']
# [request.form["FirstName"], request.form['Last_Name']
    return redirect('/')



app.run(debug=True)