# Area of a three sided triangle
import math

a = float(input("Enter the length of side a :"))
b = float(input("Enter the length of side b :"))
c = float(input("Enter the length of side c :"))

s = (a + b + c) / 2


area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print('The area of the triangle is ', area)

# Area of a two sided triangle
#a = float(input("Enter the base :"))
#b = float(input("Enter the heigth:"))

#class Triangle :
    #def area(self,a,b):
       # return a*b*0.5

#c = Triangle()
#print(c.area(56,8))



