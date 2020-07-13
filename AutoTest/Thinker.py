#coding=UTF-8
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from AutoTest.AutoMain import StartMain

root= Tk()
root.title("窗口标题")
# 窗口大小是否可以改变，宽，高,True表示可以改变
root.resizable(False, False)
root.minsize(600, 500)
#多行文本
monty =ttk.LabelFrame(root, text="运行结果") # 创建一个容器，其父容器为win
monty.grid(column=0, row=1, padx=1, pady=4)
scr = scrolledtext.ScrolledText(monty, width=60, height=50, wrap=WORD)
scr.grid(column=0, columnspan=3)
#按钮事件
but1=Button(root, text='开始',width=10,height=1,command=lambda:StartMain.Start(scr))  #带参数时必须加lambda
# but1=Button(root, text='开始',width=10,height=1) #不带参数可以使用command=方法名或注释中的方法
# but1.bind('<Button-1>',StartMain.Start)
but1.grid(column=0, row=0, padx=1, pady=4)
root.mainloop()