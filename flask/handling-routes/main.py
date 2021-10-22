from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1>Welcome to home page</h1>" #render_template('index.html')

@app.route('/about')
def about_page():
    return "<h1>This is my about page</h1>"

@app.route('/error')
def error_page():
    return "<h1>Either you run into an error or you are not authorized</h1>"

# redirection
@app.route('/admin')
def admin_page():
    return redirect(url_for('error_page'))

# dynamic path
# return html directly as string
@app.route('/<name>')
def greet(name):
    greet_format = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Greeting Page</title>
        </head>
        <body>
            <h1>Hello, { name }!</h1>
            <h1>Welcome to my Greeting Page</h1>
        </body>
        </html>"""
    return greet_format

"""since the above decorator has also the same route, one should be commented
but even uncommented, unless the function names are different, code will work 
without raising an error. in that case the above function will return the page. """
# return html as jinja template
@app.route('/<name>')
def greeting(name):
    return render_template('greet.html', arg_name=name)

# redirect to dynamic path, giving the 'name' variable from here
@app.route('/greet_admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin!!!'))

@app.route('/list10')
def list10():
    return render_template('list10.html')

@app.route('/evens')
def evens():
    return render_template('evens.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

