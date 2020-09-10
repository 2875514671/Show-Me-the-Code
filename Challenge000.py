# -*- coding: utf-8 -*-
# @Time :  11:47
# @AUTHOR : yusheng
# @File : Challenge000.py
# @SoftWore : PyCharm
"""
http://www.pythonchallenge.com/pc/def/0.html
https://www.hackingnote.com/en/python-challenge-solutions/level-0
38是一个很好的（随机的）示例，它显示了int类型在Python中可以无穷大
"""


a = 2 ** 38
print(a)

b = pow(2, 38)
print(b)

# 乘以2等于将二进制表示左移一
c = 1 << 38
print(c)
