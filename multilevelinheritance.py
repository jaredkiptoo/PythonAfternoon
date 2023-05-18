class Employee :
    def task(self):
        print("Employees")

class Manager(Employee) :
    def role(self):
        print("Managers")

class Chef(Manager):
    def info(self):
        print("Works at a hotel")

c = Chef()
c.role()