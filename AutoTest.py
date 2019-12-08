#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 22:24
# @Author  : pxg
# @File    : AutoTest.py
from appium import webdriver
import  time

desired_caps={
  "platformName": "Android",
  "platformVersion": "5.0",
  "deviceName": "GIEQM7DIZTAYY98L",
  "appPackage": "com.sina.weibo",
  "appActivity": ".SplashActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
# 等待时间
time.sleep(5)
el1 = driver.find_element_by_id("android:id/button1")
el1.click()
# 等待时间
time.sleep(5)
el2 = driver.find_element_by_accessibility_id("我的资料")
el2.click()
el3 = driver.find_element_by_id("com.sina.weibo:id/btn_login")
el3.click()

