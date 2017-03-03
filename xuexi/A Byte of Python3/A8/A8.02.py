def shuZi(a, b):
	if a < b:
		s = a + b
		print(s)
	elif a == b:
		s = a * b
		print(s)
	else:
		s = a - b
		print(s)

n = shuZi(5, 3)
q = shuZi(10, 21)
w = shuZi(3, 3)

x = 6
y = 8
shuZi(x, y)