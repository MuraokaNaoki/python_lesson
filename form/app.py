from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pykakasi
import os


app = Flask(__name__)

class Kakashi:
    
    kakasi = pykakasi.kakasi()
    kakasi.setMode('H','a')
    kakasi.setMode('K','a')
    kakasi.setMode('J','a')
    conv = kakasi.getConverter()

    @classmethod
    def japanese_to_ascii(cls,japanese):
        return cls.conv.do(japanese)

class UserInfo:
    def __init__(self, last_name, first_name, job, gender, message):
        self.last_name = last_name
        self.first_name = first_name
        self.job = job
        self.gender = gender
        self.message = message

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    print(request.full_path)
    print(request.args)
    print(request.method)
    # user_info = UserInfo(
    #     request.args.get("last_name"),
    #     request.args.get("first_name"),
    #     request.args.get("job"),
    #     request.args.get("gender"),
    #     request.args.get("message"),
    # )
    user_info = UserInfo(
        request.form.get("last_name"),
        request.form.get("first_name"),
        request.form.get("job"),
        request.form.get("gender"),
        request.form.get("message"),
    )
    return render_template("home.html", user_info=user_info)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        file = request.files['file'] #ファイルの取得
        ascii_filename = Kakashi.japanese_to_ascii(file.name)
        save_filename = secure_filename(ascii_filename) #セキュリティに問題のない名前に変換
        file.save(os.path.join('./static/image', save_filename)) #./static/image/save_filenameに画像を保存
        return redirect(url_for('upload_file', filename = save_filename))

@app.route("/upload_file/<string:filename>")
def upload_file(filename):
    return render_template('uploaded_file.html', filenam=filename)

if __name__ == "__main__":
    app.run(debug = "True")