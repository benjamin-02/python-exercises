from flask import Flask, request, render_template

app = Flask(__name__)

# lcm finds "Least Common Multiple" values of given tw  numbers
def lcm(num1, num2):
    common_multiplication = []
    for i in range(max(num1,num2), num1*num2+1):
        if i % num1 == 0 and i % num2 == 0:
            common_multiplication.append(i)
    return min(common_multiplication)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc", methods = ["GET", "POST"])
def calculate():
    if request.method == "POST":
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        try:
            result=lcm(int(num1),int(num2))
        except ValueError:
            return render_template('index.html')
        
        return render_template("result.html", var1=num1, var2=num2, result=result, developer_name="Benjamin")
    
    else:
        return render_template("result.html", developer_name="Benjamin")


if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)
