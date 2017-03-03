import easygui
import time
# easygui.msgbox('hello world')
# easygui.enterbox('请输入账号')
# easygui.buttonbox('what?')
# name = easygui.enterbox("what's your name")
# easygui.msgbox('You entered ' + name)
# name = easygui.buttonbox("What's your name", choices= ['Vanilla', 'Chocolate', 'Strawberry'])
# easygui.msgbox("You picked " + name)

i = 1
while 1:
	easygui.msgbox("别忘了打卡！", title="提醒", ok_button="知道啦")
	i += 1
	time.sleep(10)