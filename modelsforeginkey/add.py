from model import db, Employee, Project, Company

#Create Employee
john = Employee('john')
adam = Employee('adam')

#add employee
db.session.add_all([john, adam])
db.session.commit()

#create Company
company1 = Company('Microsoft', john.id)
company2 = Company('Apple', adam.id)

#add Company
db.session.add_all([company1, company2])
db.session.commit()

#create projects
john_project1 = Project('word Project', john.id)
john_project2 = Project('excel Project', john.id)
adam_project1 = Project('mac', adam.id)
adam_project2 = Project('iphone', adam.id)

#add projects
db.session.add_all([john_project1, john_project2, adam_project1, adam_project2])
db.session.commit()


