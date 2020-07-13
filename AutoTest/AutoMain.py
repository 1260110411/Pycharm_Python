#coding=UTF-8
from tkinter import *
from tkinter import scrolledtext
from AutoTest.BeginSoft import *


class StartMain:
   def Start(scr):
      scr.insert(END, Begin.SubProcess())

      return True

if __name__ == "__main__":
   root = Tk()
   root.title("窗口标题")
   # 窗口大小是否可以改变，宽，高,True表示可以改变
   root.resizable(False, False)
   root.minsize(600, 500)
   scr = scrolledtext.ScrolledText(root, width=60, height=50, wrap=WORD)
   scr.grid(column=0, columnspan=3)
   root.mainloop()
   StartMain.Start(scr)