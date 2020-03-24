#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 10:04
# @Author  : pxg
# @File    : 静态方法.py

class TOOL(object):

    count=0
    def __init__(self,name):
        self.name=name;
        TOOL.count+=1;

    @staticmethod
    def fire():
        TOOL.count+=2;

if __name__=="__main__":
    TOOL.fire();
    print(TOOL.count)

