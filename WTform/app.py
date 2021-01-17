from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form

app = Flask(__name__)

app.config['SECERET_KEY'] = b'\xf4\xbc\xfdT\xde2\xb7\xc8\x8b\xe5aC\xbbk\xd3\x85'

class UserForm(Form):
    name = StringField('名前')
    age = IntegerField('年齢')#IntegerFieldにすると数字として入力されなかったものはエラーになるようになっている
    submit = SubmitField('submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    name = age = ''
    form  = UserForm(request.form)
    if request.method == 'POST': #ユーザーが入力した情報を取得して、UserFormクラスに格納してくれる
        if form.validate(): #ユーザが入力した値が正しいのかチェックするのに有効
            name = form.name.data
            age = form.age.data
            form.name.data = ''
            form.age.data = ''
        else:
            print('入力内容に問題があります')

    return render_template('index.html', form=form, name=name, age=age)

if __name__ == '__main__':
    app.run(debug  = 'True')
