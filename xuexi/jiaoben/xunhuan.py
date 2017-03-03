# for i in range(0,10):
# 	for x in range(0,10):
# 		s = i * x
# 		print(s)


i = 1
x = 1

while i < 10:
	while x < 10:
		s = i * x
		i += 1
		x = i + 1
		print(s)