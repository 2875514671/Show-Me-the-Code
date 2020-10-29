# -*- coding: utf-8 -*-
# @Time :  15:47
# @AUTHOR : yusheng
# @File : Challenge009.py
# @SoftWore : PyCharm
from itertools import groupby
from functools import reduce
import pysnooper
import re

"""
https://www.hackingnote.com/en/python-challenge-solutions/level-10
外观序列：
a = [1, 11, 21, 1211, 111221,
https://en.wikipedia.org/wiki/Look-and-say_sequence
"""


@pysnooper.snoop()
def one():
    x = '1'
    for n in range(30):
        x = "".join([str(len(j) + 1) + i for i, j in re.findall(r"(\d)(\1*)", x)])  # re正则表达式 返回 x 的(数量，长度)(外观序列)
    # print(len(x))
    return len(x)


@pysnooper.snoop()
def two():
    x = '1'
    for n in range(30):
        x = "".join([str(len(list(j))) + i for i, j in itertools.groupby(x)])
        return len(x)


@pysnooper.snoop()
def three():
    s = len(reduce(lambda x, n:reduce(lambda a, b: a + str(len(list(b[1]))) + b[0], groupby(x), ""), range(30), "1"))
    print(s)
    return s


if __name__ == '__main__':
    one()
    two()
    three()