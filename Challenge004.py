# -*- coding = utf-8 -*-
# @Author   : YuSheng
# @Time     : 2020-09-04 14:21:27
# @File     : Challenge004.py
# @SoftWare : Sublime Text3
"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
https://www.hackingnote.com/en/python-challenge-solutions/level-4/
"""

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
    # 注意.group(0)将返回与模式匹配的整个文本，而捕获的段将从.group (1) 开始
    num = match.group(1)
