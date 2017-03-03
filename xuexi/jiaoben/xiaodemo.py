# python 入门小demo
#
# eidogo.com 里的围棋定式的解析程序，用的是 python ，为了改写，初步接触了一下 python
#
# 写了个小 demo，涉及到文件操作，时间操作，函数。基本上够用了。
#
# 在命令行里，输入 python fw.py 即可运行。
#

import time
def file_append(file, data):
    file.write(data)
    file.write('\r\n')

file = open('fw1.txt', 'a')
# file = open('fw1.txt')
# file.seek(5)
# file.write('hello, hello\r\n')
file_append(file, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
file_append(file, 'hello, hello')
file_append(file, 'hello, hello')
file.close()

