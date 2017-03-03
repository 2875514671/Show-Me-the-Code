import sys

print( "script name is", sys.argv[0]) # 使用sys.argv[0]采集脚本名称
if len(sys.argv) > 1:
	print("there are", len(sys.argv)-1, "arguments:") # 使用len(sys.argv)-1采集参数个数-1为减去[0]脚本名称

for arg in sys.argv[1:]:		#输出除了[0]外所有参数
	print(arg)

else:
	print("there are no arguments!")

