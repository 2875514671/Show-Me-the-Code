# -*- coding: UTF-8 -*-
import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH = lambda p: os.path.abspath(
	os.path.join(os.path.dirname(__file__), p)
)
global driver


class LoginAndroidTests(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['device'] = 'android'
		desired_caps['platformName'] = 'Android'
		desired_caps['browserName'] = ''
		desired_caps['version'] = '4.4.2'
		desired_caps['deviceName'] = 'HM 1SL TETD'  # 这是测试机的型号，可以查看手机的关于本机选项获得

		desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')  # 被测试的App在电脑上的位置

		# 如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
		# desired_caps['appPackage']='com.subject.zhongchou'
		# desired_caps['appActivity']='.ZhongChou'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		self.driver.quit()

	def test_login(self):
		time.sleep(10)
		# 点击“注册登录”按钮        button=self.driver.find_element_by_id("com.subject.zhongchou:id/register_button")
		button.click()
		time.sleep(5)
		# 登录
		name = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_phone')
		name.click()
		name.send_keys('183XXXXXX05')

		psd = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_password')
		psd.click()
		psd.send_keys("XXXXXXXX")

		blogin = self.driver.find_element_by_id('com.subject.zhongchou:id/go_numberlogin')
		blogin.click()
		time.sleep(10)
		# 此处加上检测登录是否成功的代码
		if __name__ == '__main__':
			suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
		unittest.TextTestRunner(verbosity=2).run(suite)