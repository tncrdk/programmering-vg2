
def foo(func):
	def wrapper(*args):
		print("Started")
		func(*args)
		print("Ended")

	return wrapper

@foo
def f(*args):
	for x in args:
		print(x)

print(f)

f = foo(f)

print(f)

f(1, 2, 3)
