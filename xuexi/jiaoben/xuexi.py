def age(n):
	c = 10
	if n > 1:
		c = age(n-1) + 2
	else:
		pass
	return c
print(age)