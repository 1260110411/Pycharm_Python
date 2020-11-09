#coding=UTF-8
import matplotlib
import matplotlib.pyplot as plt
import tkinter
from mpl_toolkits.mplot3d import Axes3D

class Analyze():
    def diagram(self,x,y):
        '''绘制二维图方法
        :param x: x轴数据,数据为数组或元组列表
        :param y: y轴数据,数据为数组或元组列表
        '''
        if len(x)==len(y):
            matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
            matplotlib.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题

            fig = plt.figure()
            fig.suptitle('方法调用次数分析曲线图', fontsize = 14, fontweight='bold')
            ax = fig.add_subplot(1, 1, 1) #仅绘制一个图形，图形显示在第一个
            ax.set_xlabel("方法名称")
            ax.set_ylabel("调用-次数")
            ax.set_title("二维图")
            plt.plot(x,y)
            plt.show()
            plt.savefig('二维图.jpg')
        else:
            Analyze.Remind("错误提示框", "输入数据长度不一致！")
    def ThreedimensionalDdiagram(self,x,y,z):
        ''' 绘制三维图方法

        :param x:
        :param y:
        :param z:
        :return:
        '''
        matplotlib.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection='3d')
        ax.plot(x,y,z)
        ax.legend()
        plt.show()
        plt.savefig('三维分析曲线.jpg')

    def Remind(self,attribute,msg):
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
    a=Analyze()
    a.ThreedimensionalDdiagram((1,2,3),(1,2,3),(123,34,34))