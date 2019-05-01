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
    if "info" not in session:
        session['info'] = ""
    else:
        for x in session['info']:
            if x == "pizza":
                x = "pumpkin pie"
    ##########################
    #Important!
    #Fix the above code.....
    # Session['info'] should display "pumkin pie" and NOT "pizza"
    #########################

    return render_template("index.html", info=session['info'])


@app.route("/form", methods=['post'])
def forms():
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = [str(request.form["FirstName"]), str(request.form['LastName']), str(request.form['FaveSnack'])]
        session['info'].pop()
        session['info'].append(str('Pumpkin Pie'))
        flash(session['info'])
        
    return redirect('/')



app.run(debug=True)