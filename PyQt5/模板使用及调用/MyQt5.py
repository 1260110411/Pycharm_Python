#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 9:38
# @Author  : pxg
# @File    : pyqt5模板.py

# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys
#sys.path.append('/PyQt5/模板使用及调用/')
import PyQt5面向对象写法

# 1.创建一个应用程序对象
app=QApplication(sys.argv)

# 2.控件的操作
#   2.1. 创建控件
#window =QWidget()
window = PyQt5面向对象写法.Window()#调用自己封装的PYQT5方法
# #   2.2. 设置控件
# window.setWindowTitle("面向对象写法")
# window.resize(500,500)
#
# #     2.2.1. 面向对象写法
#
#
#   2.3. 控件展示
window.show()
# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())

