from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1>こんにちは</h1>"

@app.route("/hello/<string:name_a>/<string:name_b>")
def show_name(name_a, name_b):
    return "<h1>こんにちは{}さん{}さん</h1>".format(name_a, name_b)

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    sum = num1 + num2
    return "<h1>{}</h1>".format(sum)

@app.route("/div/<float:num1>/<float:num2>")
def devide(num1, num2):
    result = num1/num2
    return "<h1>{}</h1>".format(result)

if __name__ == "__main__":
    app.run(debug = True)
