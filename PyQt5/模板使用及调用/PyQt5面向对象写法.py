#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 10:11
# @Author  : pxg
# @File    : PyQt5面向对象写法.py
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):  #创建父类模板
        super().__init__()
        self.setWindowTitle("QYPT5")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self): #在父类模板中添加新控件
        label=QLabel(self)
        label.setText("xxx")

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())

