#7b
class Employee:
    def __init__(self):
        self.name=" "
        self.eid=" "
        self.dept=" "
        self.salary=0
    def getdetails(self):
        self.name=input("enter name: ")
        self.eid=input("enter employee id: ")
        self.dept=input("enter employee department: ")
        self.salary=input("enter current salary: ")
    def showdetails(self):
        print("EMPLOYEE DETAILS:")
        print("Name: ",self.name)
        print("Employee id: ",self.eid)
        print("Department: ",self.dept)
        print("Salary: ",self.salary)
    def uSalary(self):
        self.salary=int(input("enter new salary: "))
        print("Updated salary: ",self.salary)
e1=Employee()
e1.getdetails()
e1.showdetails()
e1.uSalary()