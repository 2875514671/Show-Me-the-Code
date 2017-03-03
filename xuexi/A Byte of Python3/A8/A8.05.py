def shuZi():
	x = 2
	print(x)

	def ziFu():
		nonlocal x
		x = 3

	ziFu()
	print(x)

shuZi()