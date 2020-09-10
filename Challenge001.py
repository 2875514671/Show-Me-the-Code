# -*- coding: utf-8 -*-
# @Time :  15:53
# @AUTHOR : yusheng
# @File : Challenge001.py
# @SoftWore : PyCharm
"""
http://www.pythonchallenge.com/pc/def/map.html
https://www.hackingnote.com/en/python-challenge-solutions/level-1
https://www.runoob.com/python3/python3-string-maketrans.html
ord()：字符到整数
chr()：整数到字符
"""
import pysnooper


# 1. 循环
@pysnooper.snoop()
def string_result(raws):
    result = ""
    for c in raws:
        if 'a' <= c <= 'z':
            result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
        else:
            result += c
    print(result)
    return result


# 2. 列表
@pysnooper.snoop()
def string_list(raws):
    result = ''.join([chr(((ord(c) + 2) - ord('a')) % 26 + ord('a')) if 'a' <= c <= 'z' else c for c in raws])
    print(result)
    return result


# 3. str.maketrans()或bytes.maketrans()
@pysnooper.snoop()
def string_maketrans(raws):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    result = raws.translate(table)
    print(result)
    return result


# 4. str.maketrans()
@pysnooper.snoop()
def rewrite_maketrans(raws):
    a = "abcdefghijklmnopqrstuvwxyz,. '()"
    b = "cdefghijklmnopqrstuvwxyzab,. '()"
    # c = list(zip(a, b))
    d = dict(zip(a, b))
    result = "".join([d[x] for x in raws])
    print(result)
    return result


if __name__ == '__main__':
    # raw = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr
    # ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """
    raw = "map"
    string_result(raw)
    string_list(raw)
    string_maketrans(raw)
    rewrite_maketrans(raw)
