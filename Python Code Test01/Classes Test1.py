# -*- coding: utf
class Prøve1:
    def __init__(selv, name, age):
        selv.name = name
        selv.age = age
        
    def Function1(self):
        return "My name is " + self.name
    
        

p1 = Prøve1("John", 36)

print(p1.Function1())

print(Prøve1.Function1(p1))

print(p1.age)

#A new Class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + ",")
  def myfunc2(self):
  	print("and I am " + str(self.age) + " years old.")

p1 = Person("John", 36)
p2 = Person("Per", 51)

print()

p1.myfunc()
p1.myfunc2()

print()

p2.myfunc()
p2.myfunc2()

