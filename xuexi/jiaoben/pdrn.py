year = int(input('year:\n'))
#leap = 0
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
	print("这一年是闰年.")
else:
	print("这一年不是闰年.")