
def Soo():
	x = 3

	def Foo():
		x = 5
		print(x)

	Foo()

	print(x)

Soo()
