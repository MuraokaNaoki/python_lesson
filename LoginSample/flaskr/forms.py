#ログイン用のフォームと、ユーザを登録するためのフォームを定義する

from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User

#ログイン画面で利用する

class LoginForm(Form):
    email = StringField('メール:', validators = [DataRequired(), Email()])
    password = PasswordField('パスワード:', validators=[DataRequired()])
    submit = SubmitField('ログイン')

#登録画面で利用する
class RegisterForm(Form):
    email = StringField('メール: ', validators = [DataRequired(), Email('メールアドレスが誤っています')])
    username = StringField('名前: ', validators = [DataRequired()])
    password = PasswordField('パスワード: ', validators = [DataRequired(), EqualTo("password_confirm", message='パスワードが一致しません')])
    #↑EqualToではpassword_confirmで再入力したパスワードと一致しているか確認する、もし一致していない場合の出力は第２引数にメッセージとして記述
    password_confirm = PasswordField('パスワード確認: ', validators = [DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('そのメールアドレスはすでに登録されています')