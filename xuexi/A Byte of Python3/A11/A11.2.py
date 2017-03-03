#!/usr/bin/python
# Filename: backup_ver1.py

import os
# OS模块简单的来说它是一个Python的系统编程的操作模块，可以处理文件和目录这些我们日常手动需要做的操作。

import time
from datetime import datetime

# 1. 指定要备份的文件和目录.

source ='C:\\Users\\yu\\Desktop\\首展'

# 注意我们必须使用双斜杠对单斜杠进行转义.

# 2. 备份必须存储在主备份目录中

target_dir = 'E:\\备份\\'

# 记得你将使用什么改变这个,

# 3. 文件备份到一个zip文件.

# 4. zip归档文件的名称是当前的日期和时间

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. 我们使用zip命令把文件归档为zip文件

zip_command = "zip -qr %s %s" % (target, ''.join(source))

# 运行备份

print("Zip command is:")

print(zip_command)

print('starttime:', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if os.system(zip_command) == 0:

	print('Successful backup to', target)

else:

	print('Backup FAILED')

print('endtime:', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))








