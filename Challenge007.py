# -*- coding: utf-8 -*-
# @Time :  11:52
# @AUTHOR : yusheng
# @File : Challenge007.py
# @SoftWore : PyCharm
"""
http://www.pythonchallenge.com/pc/def/oxygen.html
https://www.hackingnote.com/en/python-challenge-solutions/level-7
https://docs.python.org/zh-cn/3.7/library/io.html
"""
# pillow 是 PIL 派生的库，所以要导入PIL中的Image
from PIL import Image
import requests
from io import BytesIO
import re
from urllib.request import urlopen
import png


class Oxygen:

    # 第一种方法，使用 pillow 模块
    @staticmethod
    def avoid_images(uri):
        html = requests.request('get', uri)
        # BytesIO将二进制图片信息转换为二进制流传递给Image模块处理
        img = Image.open(BytesIO(html.content))
        rows = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
        row = rows[::7]
        ords = [r for r, g, b, a in row if r == g == b]
        result = "".join(map(chr, ords))
        num = re.findall("\\d+", result)
        last_result = "".join(map(chr, map(int, num)))
        print(last_result)
        return last_result

    # 第二种方法，使用 PyPNG 模块
    @staticmethod
    def resolution(uri):
        response = urlopen(uri)
        """
        png.read()方法返回一个包含以下内容的4元组：
        width：PNG图像的宽度，以像素为单位；
        height：PNG图像的像素高度；
        rows：行数据的序列或迭代器；
        info：包含大量图像元数据的信息字典
        """
        (w, h, rgba, dummy) = png.Reader(response).read()
        # print((w, h, rgba, dummy))
        # print(w)
        # print(h)
        # print(rgba)
        # print(dummy)
        it = list(rgba)
        mid = int(h/2)
        l = len(it[mid])
        res = [chr(it[mid][i]) for i in range(0, l, 4*7) if it[mid][i] == it[mid][i + 1] == it[mid][i + 2]]
        result = "".join(map(chr, map(int, re.findall("\\d+", "".join(res)))))
        print(result)


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    ox = Oxygen()
    ox.avoid_images(url)
    ox.resolution(url)
