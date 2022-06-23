
def foo(x):
	return 2*x

def foo(x, y):
	return x + y

a = foo

print(foo)

def foo(x, y):
	return x + y

foo(2, 3)
a(2, 3)

print("a: ", a)
print("foo: ", foo)