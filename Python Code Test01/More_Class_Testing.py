
class Person:
	school_count = {}
	course_teachers = {}

	def __init__(self, fname, lname, age, school):
		self.fname = fname
		self.lname = lname
		self.age = age
		self.school = school
		self.email = f'{self.fname.lower()}.{self.lname.lower()}@{self.school.replace(" ", "_").lower()}.com'

		if self.school in Person.school_count.keys():
			Person.school_count[self.school] += 1
		else:
			Person.school_count[self.school] = 1


	def contact_info(self):
		print(f'{self.fname} {self.lname} --- {self.email}')


	@classmethod
	def get_school_population(cls, *schools_filter):
		if bool(schools_filter):
			exists = False
			for school in schools_filter:
				if school in Person.school_count.keys():
					print(f'{school}: {Person.school_count[school]}')
					print("----------------------")
					exists = True

			if not exists:
				print("No schools matched the filter")
		
		else:
			for school, population in Person.school_count.items():
					print(f'{school}: {population}')
					print("----------------------")


class Student(Person):
	course_attendants = {}

	def __init__(self, fname, lname, age, school, main_class, courses: list = None):
		super().__init__(fname, lname, age, school)
		self.main_class = main_class
		
		if courses == None:
			courses = []
		else:
			self.courses = courses

			for course in self.courses:
				if course in Student.course_attendants.keys():
					Student.course_attendants[course] += 1
				else:
					Student.course_attendants[course] = 


p1 = Person("Per", "Persson", 40, "VGS")
p2 = Person("Pål", "Persson", 30, "TG")

stud1 = Student("Espen", "Askeladden", "15", "Sandnes Ungdomskole", "1STA", ["math", "physics"])
stud2 = Student("Peer", "Gynt", "20", "Sandnes VGS", "VSCFI", ["math", "stupidity"])
stud2 = Student("Kari", "Nordmann", "20", "Sandnes VGS", "VSCFI", ["math", "stupidity", "physics"])

stud2.contact_info()
print(Student.course_attendants)
Student.get_school_population()

