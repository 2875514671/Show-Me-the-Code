def shuZi(a = 1, *bs, **cs):
	y = a
	for b in bs:
		y += b
	for c in cs:
		y += cs[c]
	return y

print(shuZi(10, 1, 12, 13, i = 100, x = 1000))
print(shuZi(10, 1, 1, 1, i = 100, x = 1000))