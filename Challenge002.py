# -*- coding: utf-8 -*-
# @Time :  17:33
# @AUTHOR : yusheng
# @File : Challenge002.py
# @SoftWore : PyCharm

import pysnooper
import requests
import re


@pysnooper.snoop()
def request_challenge(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


@pysnooper.snoop()
def get_text(html):
    comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
    data = comments[-1]
    return data


@pysnooper.snoop()
def search_text(data):
    count = {}
    for c in data:
        count[c] = count.get(c, 0) + 1
    print(count)
    return count


@pysnooper.snoop()
def adjustment_text(text):
    pass



def main():
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    html = request_challenge(url)
    data = get_text(html)
    text = search_text(data)
    adjustment_text(text)


if __name__ == '__main__':
    main()