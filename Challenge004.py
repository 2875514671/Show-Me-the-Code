# -*- coding = utf-8 -*-
# @Author   : YuSheng
# @Time     : 2020-09-04 14:21:27
# @File     : Challenge004.py
# @SoftWare : Sublime Text3


import requests
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
# num = '12345'
num = str(16044/2)

pattern = re.compile("and the next nothing is (\\d+)")

while True:
    html = (requests.get(url + num)).text
    print(html)
    match = pattern.search(html)
    if match is None:
        break
    num = match.group(1)
