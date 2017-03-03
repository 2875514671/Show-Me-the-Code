x = 50

def func():
	global x

	print(x)
	x = 2
	print(x)

func()
print(x)