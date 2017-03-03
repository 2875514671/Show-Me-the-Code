# -*- unicode: UTF-8 -*-
import re
# Python通过re模块提供对正则表达式的支持
import urllib.request
# urllib的request模块请求网页并且抓取URL内容
from bs4 import BeautifulSoup
# Python解释器 最主要的功能是从网页抓取数据
url = 'http://www.dfwsgroup.com/company/'  # 地址
# def getHtml(url):
page = urllib.request.urlopen(url)
# 打开传入的URL
html = page.read() # 读取传入的url内容
# print(html)
	# return html
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
	#通过html.parser方法解析html
# soup 是BeautifulSoup处理格式化后的字符串
# divlist = soup.find_all('div', class_='d_post_content j_d_post_content ')
print(soup)


