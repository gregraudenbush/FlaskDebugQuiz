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
    
	# print session['info']
	# print session['FaveSnack']
	if "info" not in session:
		session['info'] = ""
	# else:
	# 	for x in session['info']:
	# 		if x == 'pizza':
	# 			x= 'pumpkin pie'
    ##########################
    #Important!
    #Fix the above code.....
    # Session['info'] should display "pumkin pie" and NOT "pizza"
    #########################
	print "home page loaded"
    
	return render_template("index.html", info = session['info'])


@app.route("/form", methods=["POST"])
def form():
    print "entry completed"
    if len(request.form['FirstName']) < 1 or len(request.form['Last_Name']) < 1:
        flash("Please Complete Form")
    else:
        session['FirstName']= request.form['FirstName']
        session['FaveSnack'] = request.form['FaveSnack']
        session['LastName']=request.form['Last_Name']
        session['info'] = [session['FirstName'],session['FaveSnack'],session['LastName']]
        name = request.form["FaveSnack"]
        print name
        print session['info']

    return redirect('/')



app.run(debug=True)