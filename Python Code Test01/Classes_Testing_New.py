Tom = "HAHA"
Foo = "HIHI"


class students:
	school = "VGS"

	def __init__(self, first, last, *titles, **grades):
		self.oogie = first
		self.boogie = last

		self.titles = titles if titles else None
		self.grades = grades if grades else {}

	
	@staticmethod
	def foo(*args):
		for i in args:
			print(i)
		
		print("--------------------------")

	
	def show_titles(self):
		print(f"{self.oogie} {self.boogie} Titles:")
		if self.titles:
			for title in self.titles:
				print(title)
		else:
			print(self.titles)
		
		print("--------------------------")

	
	def show_grades(self):
		print(f'({self.oogie} {self.boogie}) Grades: ')
		for subject, grade in self.grades.items():
			print(f'{subject}: {grade}')
		
		print("-----------------------")

	
	@classmethod
	def set_school(cls, new_school):
		cls.school = new_school

	
	@staticmethod
	def day_today():
		print("Dag: (func funker ikke)")
		print("Søndag")
		
		print("-----------------------")


student1 = students(Tom, Foo, Math = 1, Physics = 1)
student2 = students("Tom", "Foo", "Worst", Science = 1)

student2.email = student2.oogie + "." + student1.boogie + "@gmail.com"

	
student1.show_grades()
student2.show_grades()
student1.show_titles()
student1.day_today()
student1.foo("Hello", "Hei", "Salut")