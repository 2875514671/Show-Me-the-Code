# -*- coding: utf-8 -*-
# @Date    : 2020-09-09 10:38:49
# @Author  : YuSheng
# @Software: Sublime Text3
# @FileName : Challenge006.py
"""
https://www.hackingnote.com/en/python-challenge-solutions/level-6
ZipFile.comment：与ZIP文件关联的注释。
ZipInfo.comment：单个存档成员的注释。
"""

import zipfile
import re


def get_zipfile():

    f = zipfile.ZipFile(r"E:\IDM\IDM下载\channel.zip")

    print(f.read('redame.txt').decode("utf-8"))

    num = '90052'

    comments = []

    while True:

        content = f.read(num + '.txt').decode('utf-8')

        comments.append(f.getinfo(num + ".txt").comment.decode('utf-8'))

        match = re.search("Next nothing is (\\d+)", content)

        if match is None:

            break

        num = match.group(1)

    print("".join(comments))


if __name__ == '__main__':
    get_zipfile()
