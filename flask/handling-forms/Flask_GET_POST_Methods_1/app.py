from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/total', methods=['GET', 'POST'])
def calculate_total():
    if request.method == 'POST':
        input_tags = ('value1', 'value2', 'value3')
        try:
            numbers = [int(request.form.get(i)) for i in input_tags]
        except ValueError:
            return render_template('index.html')
        return render_template('number.html', total=sum(numbers))
    else:
        return render_template('number.html')

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)
