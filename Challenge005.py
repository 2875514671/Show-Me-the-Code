# -*- coding: utf-8 -*-
# @Date    : 2020-09-08 15:15:03
# @Author  : YuSheng
# @Software: Sublime Text3
# @FileName : Challenge005.py


from urllib.request import urlopen
import pysnooper
import pickle


# @pysnooper.snoop()
def peak(url):
    html = urlopen(url)
    data = pickle.load(html)
    for raw in data:
        solution = ''.join(k * v for k, v in raw)
        print(solution)


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    peak(url)
