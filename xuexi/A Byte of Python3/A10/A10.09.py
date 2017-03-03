# help(str)

# 在Python中有两个函数分别是startswith()函数与endswith()函数，功能都十分相似，startswith()函数判断文本是否以某个字符开始，endswith()函数判断文本是否以某个字符结束。

name = 'yushikai'

if name.startswith('yu'):
	print('Yes,the string starts with "yu"')

if 'a' in name:
	print('Yes, it contains the string "a"')

if name.endswith('kai'):
	print('Yes,the string ends with "kai')

if name.find('shi') != -1:
	print('Yes, it contains the string "shi"')
