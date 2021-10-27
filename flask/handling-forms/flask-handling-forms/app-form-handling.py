from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html", name="Benjamin")


@app.route('/greet', methods=["GET"])
def greet():
    if 'username' in request.args:
        entered_username = request.args['username']
        return render_template('greet.html', user=entered_username)
    else: 
        return '<h1>Send your user name with "username" param in query string</h1> \
               <h2>Example:   localhost:5000/greet?username=......</h2>'


@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method=="POST":
        entered_username = request.form['username']
        entered_password = request.form['password']
        if entered_password == 'MyVerySecurePassword':
            return render_template('secure.html', user=entered_username)
        else:
            return render_template('login.html', control=True, user=entered_username.title())
    else:
        return render_template('login.html', control=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
