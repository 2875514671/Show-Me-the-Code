# -*- coding = utf-8 -*-
# @Author: YuSheng
# @Date:   2020-09-02 11:20:46
# @File:   Challenge003.py
# @SoftWare  : Sublime Text3
"""
http://www.pythonchallenge.com/pc/def/equality.html
https://www.hackingnote.com/en/python-challenge-solutions/level-3

模式可以描述为[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+。这是模式的细分：
[a-z]：1个小写字母
[A-Z]： 1个大写字母
[A-Z]{3}：3个连续的大写字母
[A-Z]{3}[a-z][A-Z]{3}：3个大写字母+ 1个小写字母+ 3个大写字母
[^A-Z]：任何字符但大写字母
[^A-Z]+：至少一个这样的角色
[^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+：在我们之前和之后的其他东西（AAAbCCC），因此每边不超过3个连续的大写字母
[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+：...而我们只关心小写
"""
import pysnooper
import requests
import re


@pysnooper.snoop()
def get_text(uri):
    html = (requests.get(uri)).text
    date = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", html)
    text = "".join(date)
    print(text)
    return text


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    get_text(url)
