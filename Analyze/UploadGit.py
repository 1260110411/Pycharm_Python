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
    def UpGit(self,path,files,Message):
        try:
            from git import Repo
            # repo = Repo.init(path, bare=True)
            # assert repo.bare == True
            repo = Repo(path)
            if "origin" in repo.remotes:
               pass
            else:
              remote = repo.create_remote(name="origin", url='git@github.com:1260110411/AutoTest.git')# 推送本地分支到远程版本库
            for item in files:
                repo.index.add(item)
            # repo.create_tag('版本号V0.0.0.1')  # 创建tag
            repo.index.commit(Message)
            # print(repo.is_dirty()) #与远程服务器上的文件进行比对，如果不同则返回True
            # fileList = repo.untracked_files #获取未上传的文件列表
            # print(fileList)
            repo.remote("origin").push()
            print("文件上传完毕!")
        except Exception as ex:
            print("上传失败，异常如下："+ex)

if __name__=='__main__':
    list = []  ## 空列表
    list.append('Google')  ## 使用 append() 添加元素
    list.append('Runoob')
    print(list)

    a=[]
    a.append('image')
    a.append('test.html')
    UpLoad.UpGit("E:\Github\AutoTest\AutoTest",a,'重复文件上推')