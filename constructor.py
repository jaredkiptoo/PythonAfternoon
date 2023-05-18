class Employee :
    def __init__(self,firstname,course,age):
        self.firstname = firstname
        self.course = course
        self.age = age

    def info(self):
     print(self.firstname,self.course,self.age)

e = Employee("Jared","MIT","22")
e.info()
y = e.course
print(y)
