#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 18:05
# @Author  : pxg
# @File    : 调用QT页面.py
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.untitled import Ui_Form as ImageEditorPage


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ImageEditorPage()
        self.ui.setupUi(self)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(qApp.exec_())

