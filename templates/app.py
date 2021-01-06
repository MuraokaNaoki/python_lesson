from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
    login_user = {
    'name':user_name,
    'age':age
    }
    return render_template('home.html', login_user = login_user)

if __name__ == "__main__":
    app.run()
