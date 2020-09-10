# -*- coding: utf-8 -*-
# @Date    : 2020-09-08 15:15:03
# @Author  : YuSheng
# @Software: Sublime Text3
# @FileName : Challenge005.py
"""
http：//www.pythonchallenge.com/pc/def/peak.html
https://www.hackingnote.com/en/python-challenge-solutions/level-5
https://docs.python.org/3.7/library/pickle.html
"""
from urllib.request import urlopen
import pickle


def peak(url):
    html = urlopen(url)
    data = pickle.load(html)
    for raw in data:
        solution = ''.join(k * v for k, v in raw)
        print(solution)


if __name__ == '__main__':
    uri = 'http://www.pythonchallenge.com/pc/def/banner.p'
    peak(uri)
