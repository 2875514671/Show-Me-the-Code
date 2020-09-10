# -*- coding: utf-8 -*-
# @Time :  17:33
# @AUTHOR : yusheng
# @File : Challenge002.py
# @SoftWore : PyCharm

import pysnooper
import requests
import re


@pysnooper.snoop()
def get_result(url):
    html = (requests.get(url)).text
    data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
    word = "".join(re.findall("[A-Za-z]", data))
    print(word)
    return word


if __name__ == '__main__':
    uri = "http://www.pythonchallenge.com/pc/def/ocr.html"
    get_result(uri)
