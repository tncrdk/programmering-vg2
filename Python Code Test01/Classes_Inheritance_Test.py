
#self er en plassholder for navnet på objektet; f.eks: p1. __init__() funksjonen gir attributter til klassen. 
class Person:
    def __init__(self, fname, lname, email):
    #def createname(self, fname, lname, email):
        self.fname = fname
        self. lname = lname
        self.email = email
    
    def printfunc(abc):
        print("Name: " + abc.fname + " " + abc.lname)
        print("Email: " + abc.email)

p1 = Person("Per", "Pålsen", "per.paalsen@email.com")

#p1 = Person()
#p1.fname = "Pål"
#p1.lname = "Pålsen"
#p1.email = "Something"

p1.printfunc()

class Student(Person):
    def __init__(self, fname, lname, email, ID):
        #Person.__init__(self, fname, lname, email)
        super().__init__(fname, lname, email)
        self.ID = ID
    
    def elevID(self):
        print("ElevID " + self.ID)

p2 = Student("Pål", "Person", "paal.person@email.com", "253")
p2.printfunc()
p2.elevID()

class Teacher(Person):
    def __init__(self, fname, lname, email, ID):
        super().__init__(fname, lname, email)
        self.ID = ID
    
    def teacherID(self):
        print("LærerID " + self.ID)

p3 = Teacher("Espen", "Askeladden", "espen.askeladden@email.com", "555555")
p3.printfunc()
p3.teacherID()

