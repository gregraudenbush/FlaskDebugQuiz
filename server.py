from flask import Flask, request, redirect, session, flash, render_template


app = Flask(__name__)
app.secret_key = "unicorns"


@app.route('/')
def index():
    if "info" not in session:
        session['info'] = ""
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = [request.form["FirstName"], request.form['LastName'],
                           request.form['FaveSnack']]

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)