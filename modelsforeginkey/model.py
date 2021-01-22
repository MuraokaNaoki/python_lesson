import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))

#データベースの接続先の設定
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Employee(db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)#人の名前
    #relationを作成することでemployeesテーブルを取得した際に紐づけられたprojectsとcompanyを取得することができる
    #One to Many
    projects = db.relationship('Project', backref='employees', lazy = 'joined')#Projectクラスも取得
    #One to One
    company = db.relationship('Company', backref='employees', uselist=False)#Companyクラスも取得

    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.company:
            return f"Employee name = {self.name} company is {self.company.name}"
        else:
            return f'Employee name = {self.name}, has no company'

    def show_projects(self):
         for project in self.projects:
             print(project.name)

class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)#プロジェクトの名前
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))#employeesテーブルのidと外部キーで紐付ける

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Company(db.Model):

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)#会社の名前
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))#employeesテーブルのidと外部キーで紐付ける 

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

db.create_all()