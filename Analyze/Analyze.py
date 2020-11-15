#coding=UTF-8
import matplotlib
import matplotlib.pyplot as plt
import tkinter
from mpl_toolkits.mplot3d import Axes3D
import sqlite3
import random
import copy
import pandas as pd
import numpy as np
import datetime as T

class Analyze():
    @classmethod
    def SQLITEconn(self,sql):
        '''
        数据库连接
        :param sql: 要执行的语句
        '''
        conn = sqlite3.connect('MES_AUTOTEST.db')
        c = conn.cursor()
        result=c.execute(sql).fetchall()
        conn.commit()
        conn.close()
        return result

    @classmethod
    def diagram(self,method,MinTime,MaxTime,YMax=2):
        '''绘制二维图方法
        :param x: x轴数据,数据为数组或元组列表
        :param y: y轴数据,数据为数组或元组列表
        '''
        # if len(x)==len(y):
        matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
        matplotlib.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题

        fig = plt.figure()
        fig.suptitle('方法调用次数分析曲线图', fontsize = 14, fontweight='bold')
        ax = fig.add_subplot(1, 1, 1) #仅绘制一个图形，图形显示在第一个
        ax.set_xlabel("时间")
        ax.set_ylabel("次数")
        ax.set_title("二维图")
        x_time = pd.date_range(start=MinTime, end=MaxTime, freq='min')
        for key in method:
            c=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
            i=0
            yi = []  # Y轴坐标
            while i<len(x_time):
                xi=T.datetime.strftime(x_time[i],'%Y-%m-%d %H:%M') #将时间转换为字符串
                if xi in method[key][0]:
                    plt.scatter(x_time[i],method[key][1][method[key][0].index(xi)],color=c) #将时间对应的索引值的次数赋给Y轴
                    yi.append(method[key][1][method[key][0].index(xi)])
                else: #某分钟没有该方法，表示数量为0
                    plt.scatter(x_time[i],0, color=c)
                    yi.append(0)
                i=i+1
            if max(yi)>=YMax:
                plt.plot(x_time, yi, c=c, label="..."+key[-6:-1],linewidth=0.5,alpha=1)
            else:
                plt.plot(x_time, yi, c=c, linewidth=0.5,alpha=0.1)
            plt.xticks(rotation=90)
        plt.plot(x_time, [YMax] * len(x_time), c='r', linestyle='--', linewidth=1)
        plt.legend(loc='upper right', fontsize=10,frameon=False)
        plt.show()
        fig.savefig(r'E:\Github\AutoTest\AutoTest\二维图.jpg')
        # else:
        #     Analyze.Remind("错误提示框", "输入数据长度不一致！")

    @classmethod
    def ThreedimensionalDdiagram(self,x,y,z):
        ''' 绘制三维图方法

        :param x: x轴数据,数据为数组或元组列表
        :param y: y轴数据,数据为数组或元组列表
        :param z: z轴数据,数据为数组或元组列表
        :return:
        '''
        matplotlib.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection='3d')
        import numpy as np
        # xs = np.arange(20)
        # cs=['r', 'g', 'b', 'y']* len(xs)
        ax.bar(x, y, z,zdir='y', color='r' )
        ax.legend('ces')
        plt.show()
        fig.savefig('三维分析曲线.jpg')

    @classmethod
    def Remind(self,attribute,msg):
        '''

        :param attribute: 判断提示框的文字信息
        :param msg: 提示框描述信息
        :return: 返回结果或无
        '''
        top = tkinter.Tk()
        top.withdraw()  # 将窗口从屏幕上移除（并没有销毁），需要重新显示窗口，使用 deiconify() 方法
        top.update()
        if attribute=="提示框":
            tkinter.messagebox.showinfo("提示", msg)
        elif attribute=="警告提示框":
                tkinter.messagebox.showwarning("警告", msg)
        elif attribute=="错误提示框":
            tkinter.messagebox.showerror("错误", msg)
        elif attribute=="问题提示框":
            result=tkinter.messagebox.askquestion("提示", msg)
            return result #返回字符串yes/no
        elif attribute=="确定取消提示框":
            result=tkinter.messagebox.askokcancel("提示", msg)
            return result #返回布尔值true/false
        elif attribute=="是否提示框":
            result=tkinter.messagebox.askyesno("提示", msg)
            return result #返回布尔值true/false
        elif attribute=="是否取消提示框":
            result=tkinter.messagebox.askyesnocancel("提示", msg)
            return result #返回布尔值true/false/none
        elif attribute == "重试取消提示框":
            result = tkinter.messagebox.askretrycancel("提示", msg)
            return result  # 返回布尔值true/false
        top.destroy()

if __name__=="__main__":
    a=Analyze.SQLITEconn("select (st2.网址 || st2.方法) 方法名,st.时间,st.重复数 from statistic2  as st2 inner  join statistic as st  on  st2.网址=st.网址 and st2.方法=st.方法名称 ")
    #演示：二维图
    Method={}
    i=0
    MinTime=a[i][1]#横坐标最小值
    MaxTime = a[i][1]#横坐标最大值
    while i<len(a):
        if a[i][1]<MinTime:
           MinTime=a[i][1]
        if a[i][1]>MaxTime:
           MaxTime = a[i][1]
        if a[i][0] in Method: #方法的时间已被记录时，添加新时间和次数到Method中
            Time_mdb,Frequece_mdb=copy.deepcopy(Method[a[i][0]]) #深拷贝解决对象引用导致字典变更问题
            Time_mdb.append(a[i][1])
            Frequece_mdb.append(a[i][2])
            del Method[a[i][0]]
            Method[a[i][0]]=(Time_mdb,Frequece_mdb)
        else: #方法的时间未被记录时，添加时间和次数到Method中
            Time = []
            Frequece = []
            Time.append(a[i][1])
            Frequece.append(a[i][2])
            Method[a[i][0]] = (Time, Frequece)
        i=i+1

    Analyze.diagram(Method,MinTime,MaxTime)
    #演示：三维图-散点图
    # Analyze.ThreedimensionalDdiagram(('ceshi','ce','c12'),("gfd","fgd","dfgd"),(32,34,35))
    #演示：三维-直方图
