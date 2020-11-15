#coding=UTF-8

class CreateHTML():
    @classmethod
    def HtmlWebbrowser(self):
        import webbrowser
        GEN_HTML = r"E:\Github\AutoTest\AutoTest\test.html"# 命名生成的html
        f = open(GEN_HTML, 'w')# 打开文件，准备写入
        str1 = 'my name is :' # 准备相关变量
        str2 = '--MichaelAn--'
        message = """
        <html>
        <head></head>
        <body>
        <img src="二维图.jpg" />
        </body>
        </html>
        """ # % (str1, str2) # 写入HTML界面中
        # 写入文件
        f.write(message)
        # 关闭文件
        f.close()
        # webbrowser.open(GEN_HTML, new=1) # 运行完自动在网页中显示
class UpLoad():
    @classmethod
    def UpGit(self):
        from git import Repo
        path = "E:\Github\AutoTest\AutoTest"
        repo = Repo(path)
        print(repo.is_dirty()) #与远程服务器上的文件进行比对，如果不同则返回True
        fileList = repo.untracked_files #获取未上传的文件列表
        pass
if __name__=='__main__':
    CreateHTML.HtmlWebbrowser()