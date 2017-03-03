def zuiDa(x, y):
	'''
	打印两个数之间最大的那一个数

	文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。强烈建议你在你的函数中使用文档字符串
时遵循这个惯例。
'''
	x = int(x)
	y = int(y)
	if x > y:
		print(x)
	else:
		print(y)

zuiDa(1, 2)
print(zuiDa.__doc__)
help(zuiDa)

