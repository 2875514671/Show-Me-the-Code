# -*- coding: utf-8 -*-
# @Time :  17:33
# @AUTHOR : yusheng
# @File : Challenge002.py
# @SoftWore : PyCharm
"""
http://www.pythonchallenge.com/pc/def/ocr.html
https://www.hackingnote.com/en/python-challenge-solutions/level-2
https://docs.python.org/zh-cn/3/library/re.html
"""
import pysnooper
import requests
import re


@pysnooper.snoop()
def get_result(url):
    html = (requests.get(url)).text
    # 默认情况下，点 不匹配\n，因此需要使用 re.DOTALL
    data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
    word = "".join(re.findall("[A-Za-z]", data))
    print(word)
    return word


if __name__ == '__main__':
    uri = "http://www.pythonchallenge.com/pc/def/ocr.html"
    get_result(uri)
