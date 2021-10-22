from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return "<h1>Conditions demo</h1>"
    text = "This is a variable i defined in python"
    # text2 = "heyyy"  
    text2 = ""
    return render_template('index.html', 
                            arg_var=text,
                            arg_var2=text2)


@app.route('/list')
def my_list():
    names = ["Peter Parker", "Tony Stark", "Bruce Wayne"]
    return render_template('body.html', arg_names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
