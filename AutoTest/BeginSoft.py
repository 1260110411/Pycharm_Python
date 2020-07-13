#coding=UTF-8


class Begin:
    @staticmethod
    def OS():
        import os
        a=os.system(r'C:\Users\Public\Desktop\鲁大师.lnk')
        if a==0:
          return True
        else:
          return False

    @staticmethod
    def SubProcess():
        import subprocess
        # shell=True 表示使用终端shell执行程序，windows下面就是cmd.exe
        ret = subprocess.check_output('java -version', shell=True, encoding='gbk')
        # print(ret)
        return ret

    @staticmethod
    def Popen():
        from subprocess import Popen
        from subprocess import PIPE
        popen1 = Popen(
            args='java -version',  # args =可以省略，原因可以看看缺省参数，前面讲的有，参数传错的时候err的信息不会为 NONE
            stdout=PIPE,
            shell=True,
            encoding='gbk'
        )
        output, err = popen1.communicate()  #
        print(output)
        return output

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')

if __name__ == "__main__":
    Begin.Popen()