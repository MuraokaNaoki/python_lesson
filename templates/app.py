from flask import Flask, render_template, redirect, url_for, abort
from datetime import datetime

app = Flask(__name__)

@app.template_filter('born_year')
def calcurate_born_year(age):
    now_timestamp = datetime.now()
    return str(now_timestamp.year - int(age)) + "年"

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

class UserInfo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

@app.route('/userlist')
def user_list():
    users = [
        UserInfo("Naoki", 23), UserInfo("Taro", 21), UserInfo("Tom", 42), UserInfo("Bob", 56)
    ]
    is_login = True
    return render_template('userlist.html', users = users, is_login = is_login)

@app.route('/user/<string:user_name>/<int:age>')
def user(user_name, age):
    if user_name in ["Naoki", "Taro", "Ryo"]:
        return redirect(url_for('home', user_name = user_name, age = age))
    else:
        abort(500, "そのユーザはリダイレクトできません")

@app.errorhandler(500)
def system_error(error):
    error_description = error.description
    return render_template('system_error.html', error_description = error_description), 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'),404

if __name__ == "__main__":
    app.run(debug = "True")
