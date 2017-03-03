#!/usr/bin/python
# Filename: backup_ver2.py

import os
import time
from datetime import datetime

# 1. 指定要备份的文件和目录列表.

source = ['C:\\Users\\yu\\Desktop\\首展']

# 注意我们必须使用双斜杠对单斜杠进行转义.

# 2. 备份必须存储在主备份目录中

target_dir = 'E:\\备份'

# 记得你将使用什么改变这个

# 3. 文件备份到一个zip文件.

# 4. 当天日期是主目录的子目录的名称

today = target_dir + os.sep + time.strftime('%Y%m%d')

# 当前时间是zip归档文件的名称

now = time.strftime('%H%M%S')

# 创建子目录如果它不是已经存在

if not os.path.exists(today):

	os.mkdir(today) # make directory

print('Successfully created directory', today)

# zip文件的名称

target = today + os.sep + now + '.zip'

'''
首先，Python
 是跨平台的。
在 Windows 上，文件的路径分割符号是 '\' ，在 Linux 上 是 ‘/’。
为了让你的代码在不同的平台上都能运行，那么你写路径的时候是写 ‘/’ 还是写 '\' 呢？
使用 os.sep 的话，你就不用去考虑这个了，os.sep 根据你所处的平台，自动地采用相应的分割符号。
举例：
Linux下一个路径,  /usr/share/python，那么上面的 os.sep 就是 ‘/’
Windows下一个路径, C:\Users\Public\Desktop, 那么上面的 os.sep 就是 '\'。
''' # os.sp用法

# 5. 我们使用zip命令把文件归档为zip文件

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# 运行备份

print('starttime:', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if os.system(zip_command) == 0:

	print('Successful backup to', target)

else:

	print('Backup FAILED')

print('starttime:', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))