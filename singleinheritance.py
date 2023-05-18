class Animal :
    age = 10

    def speak(self):
        print("speaking")

class Dog(Animal) :
    def eat(self):
        print("Eating")

d = Dog()
d.speak()

print(issubclass(Dog,Animal))
print(isinstance(d,Dog))