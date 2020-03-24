#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:45
# @Author  : pxg
# @File    : selenium_test.py


#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #模拟键盘的操作需要先导入键盘模块
from selenium.webdriver.common.action_chains import ActionChains #鼠标事件需要先导入模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# time.sleep(3)
# driver.get("http://www.hordehome.com")
# time.sleep(3)
#返回上一页
# driver.back()
# time.sleep(3)
#切换到下一页
# driver.forward()
#等待5秒后刷新页面
# time.sleep(3)
# driver.refresh()
#设置窗口大小为540*960
# driver.set_window_size(540,960)
# time.sleep(3)
#将浏览器窗口最大化
# driver.maximize_window()
# time.sleep(3)
# driver.get_screenshot_as_file(r"C:\Users\PXG\Desktop\截图.png")
#关闭当前窗口
#driver.close()
#退出浏览器进程
#driver.quit()
#通过id定位百度搜索框，并输入“python”
#driver.find_element_by_id("kw").send_keys("python")

# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
#driver.find_element_by_name("wd").send_keys("python")
# a=driver.find_elements_by_tag_name("input")[0].send_keys("python")
# print(a)
#通过link(超链接)属性定位到hao123，并点击
# driver.find_element_by_link_text("hao123").click()
#partial_link是一种模糊匹配的方式，对I于超长字符串截取其中一部分
# driver.find_element_by_partial_link_text("ao123").click()
#一、xpath元素定位
# 1）可以用*号表示任意标签
#在firepath里copy出xpath地址
# driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("python")
#用xpath通过id属性定位
# driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("python")
#用xpath通过name属性定位
#driver.find_element_by_xpath("//*[@name=\"wd\"]").send_keys("python")
#用xpath通过class属性定位
# driver.find_element_by_xpath("//*[@class=\"s_ipt\"]").send_keys("python")
#用xpath通过其他属性定位（例如：autocomplete）
# driver.find_element_by_xpath("//*[@autocomplete=\"off\"]").send_keys("python")

# 2）制定具体某个标签，就可以直接写标签名称
#用xpath通过name属性定位
# driver.find_element_by_xpath("//input[@name=\"wd\"]").send_keys("python")
#用xpath通过class属性定位
# driver.find_element_by_xpath("//input[@class=\"s_ipt\"]").send_keys("python")
#用xpath通过其他属性定位（例如：autocomplete）
# driver.find_element_by_xpath("//input[@autocomplete=\"off\"]").send_keys("python")
#通过定位它老爸来定位input输入框,提示找不到，原因未知
# driver.find_element_by_xpath("//span[@class=\"bg s_ipt_wr quickdelete-wrap\"]/input").send_keys("python")
#通过定位它爷爷来定位input输入框
# driver.find_element_by_xpath("//form[@id=\"form\"]/span/input").send_keys("python")
#用xpath定位老大
# driver.find_element_by_xpath("//div[@id=\"u1\"]/a[1]").click()
#用xpath定位老二
# driver.find_element_by_xpath("//div[@id=\"u1\"]/a[2]").click()
#用xpath定位老三
# driver.find_element_by_xpath("//div[@id=\"u1\"]/a[3]").click()
#xpath逻辑运算
# driver.find_element_by_xpath("//input[@name=\"wd\" and @id=\"kw\"]").send_keys("python")
#xpath模糊匹配功能
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
#xpath也可以模糊匹配某个属性
# driver.find_element_by_xpath("//*[contains(@name,'tj_trhao123')]").click()
#xpath也可以模糊匹配什么开头
# driver.find_element_by_xpath("//*[starts-with(@id,'virus-')]").click()
#xpath也可以模糊匹配什么结尾
# driver.find_element_by_xpath("//*[ends-with(@id,'virus-')]").click()
#xpath还支持最强的正则表达式,提示异常
# driver.find_element_by_xpath("//*[matchs(text(), 'hao13')]").click()
#二、css定位语法
#css通过id属性定位
# driver.find_element_by_css_selector("#kw").send_keys("python")
#css通过class属性定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("python")
#css通过标签属性定位，这里运行会报错，主要了解这个写法
# driver.find_element_by_css_selector("input").send_keys("python")
#css通过name属性定位
# driver.find_element_by_css_selector("[name='wd']").send_keys("python")
#css通过autocomplete属性定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python")
#css通过type属性定位，目前百度输入框已经没有type的类型
# driver.find_element_by_css_selector("[type='text']").send_keys("python")
# css通过标签与属性组合来定位元素,报异常
# driver.find_element_by_css_selector("input:contains('kw')")
#css通过标签与class属性的组合定位
# driver.find_element_by_css_selector("input.s_ipt").send_keys("python")
#css通过标签与id属性的组合定位
# driver.find_element_by_css_selector("input#kw").send_keys("python")
#css通过标签与其他属性组合定位
# driver.find_element_by_css_selector("input[id='kw']").send_keys("python")
#css通过层级关系定位
# driver.find_element_by_css_selector("form#form>span>input").send_keys("python")
#css通过层级关系定位
# driver.find_element_by_css_selector("form.fm>span>input").send_keys("python")
#选择第1个a
# driver.find_element_by_css_selector("div#u1>a:nth-child(1)").click()
#选择第2个a
# driver.find_element_by_css_selector("div#u1>a:nth-child(2)").click()
#选择第3个a
# driver.find_element_by_css_selector("div#u1>a:nth-child(3)").click()
#css逻辑运算,里跟 xpath 不一样，无需写 and 关键字
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")
#三、辅助定位元素，forefox存在插件Selenium Builder
#四、操作元素（鼠标和键盘事件）
#实例：打开baidu(测试部落论坛)后，点击hao123，一般为了保证输入的正确性，可以先清空下输入框，然后输入搜索关键字
# driver.implicitly_wait(10) #隐式等待，5秒钟内只要找到了元素就开始执行,可能还没等页面元素稳定后就定位 ，导致定位不准确
# driver.find_element_by_name("tj_trhao123").click()#1.点击（鼠标左键）页面按钮：click()
# driver.find_element_by_name("word").clear() #2.请空输入框：clear()
# driver.find_element_by_name("word").send_keys("selenium")#3.输入字符串：send_keys()
#submit 提交表单,一般用于模拟回车键
# driver.implicitly_wait(10)
# driver.find_element_by_id("kw").send_keys("测试部落")
#submit()模拟enter键提交表单
# driver.find_element_by_id("kw").submit()
#模拟enter键操作回车按钮
# driver.find_element_by_id("kw").send_keys(Keys.ENTER)
# 键盘 F1 到 F12：send_keys(Keys.F1) 把 F1 改成对应的快捷键
# 复制 Ctrl+C：send_keys(Keys.CONTROL,'c')
# 粘贴 Ctrl+V：send_keys(Keys.CONTROL,'v')
# 全选 Ctrl+A：send_keys(Keys.CONTROL,'a')
# 剪切 Ctrl+X：send_keys(Keys.CONTROL,'x')
# 制表键 Tab: send_keys(Keys.TAB)
#鼠标悬停在搜索设置按钮上
# mouse=driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# 右击鼠标：context_click()
# 双击鼠标：double_click()
#获取当前窗口句柄
# h=driver.current_window_handle
# print(h)
#定位网页、贴吧等链接
# s=driver.find_element_by_css_selector("#u1>a")
# #点击第一个按钮
# s.click() #'WebElement' object does not support indexing
# all_h=driver.window_handles
# print(all_h)

# page= driver.page_source
# print(page)


#五、cookie获取
# driver=webdriver.Chrome()
#启动浏览器后获取cookies
# driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
#打开主页后获取cookie
# print(driver.get_cookies())
# driver.implicitly_wait(30)
# driver.find_element_by_id("LoginName").send_keys("爱因斯坦福大")
# driver.find_element_by_id("Password").send_keys("PXG-18710711778")
# driver.find_element_by_class_name("ladda-label").click()
# time.sleep(3)
# print(driver.get_cookies())
#清除指定name的cookie
# driver.delete_cookie(name=".Cnblogs.Account.Session")
# print(driver.get_cookies())
#清除cookie后刷新
# driver.refresh()
#清除所有cookie
# driver.delete_all_cookies()
#清理完所有cookie后，查看cookie为空
# print(driver.get_cookies())

#将抓包的cookie添加到代码的cookie中
# 单引号前加u作用：后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码

# driver.delete_cookie(name=".cnblogs.com")
# cookie1 ={u'domain': u'.cnblogs.com',
# u'name': u'.CNBlogsCookie',
# u'value': u'3F7F96FA64CCCA384624F500BCB5423E6E92CDB8FAE2D072B0F50DC53F024B297C7652F169967B218E044E7904DB1E1C9F4E031804B18B123E47C6ED5774DB31CD0B2EF305DE014F8C4ED821CF65BE2BA8BBB80E',
# u'expiry': 1491887887,
# u'path': u'/',
# u'httpOnly': True,
# u'secure': False}
# cookie2 ={u'domain': u'.cnblogs.com',
# u'name': u'.Cnblogs.AspNetCore.Cookies',
# u'value': u'CfDJ8Nf-Z6tqUPlNrwu2nvfTJEgWbolNn9sD5rVDxBLzVJWQCEXFaxwUbXOeD8GZ4boXVrP901lq6duYrDhPcoO26U33hTDvHUrXbNuNYm3X-Us3Q-xHO81CoiVzvCYjawOf7vKCjlNUaJK8Kn0wnJ-j3NiykqQsn91z430SfNHi836Xq2pVtBVBdeohpFonecFduzwmVFwx-xQZoEjR8aRYHwU7KYsQFViGpCfOXnfnPPQDnhqM6N_0dLfnA8SK5YdHOetnWvYxhru9lTHxXM1OO4do3S1NnkQbf87Z4bQ9LZ46GZuosaEJoDf3OBbb3wHjkRE2FURLSriRmccAFNrnQXFd07jybEU0iBfuEjfSEFyykwBSvm6TwGWxvp-KAJDcUTMuX-CQoNOUmFikHHsV0Nl6dH4URPFPy0HfUQeslGlJGgpbFNq29xSsupabMQlaOZTE6iyrVxT3DUhnkB04jHm4Zz0vmSWRIOHfiq4GYPksGmKuLhd3T0sHLeXV_gUnBD9YDb5Nv_gqdkWbbdUirTP5SNaUgBcKtSJkL7lIaMWlK5LbpOYC8Ux6gMnt8QGJOrL0YzpI3VSAcQzC6GssKBs',
# u'expiry': 1491887887,
# u'path': u'/',
# u'httpOnly': True,
# u'secure': False}
# driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
# a='my_cookie'
# print(driver.get_cookies(a))
# print(driver.get_cookies('.CNBlogsCookie'))
# driver.add_cookie(cookie1)#添加2个值
# driver.add_cookie(cookie1)
# time.sleep(3)
# driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
# driver.refresh() #刷新页面后就自动登录了
# print(driver.get_cookies())

#六、场景判断

driver=webdriver.Chrome()
driver.get("https://baidu.com")
time.sleep(5)
#判断元素是否存在，并返回true或false
#1）等待时长5s,默认0.5s询问一次；
#2）调用该方法提供的驱动程序作为参数，直到返回值为True
# element=WebDriverWait(driver,5).until(lambda x: x.find_element_by_id("kw"))
#1）等待时长30s；
#2）1s询问一次；
#3）超时后的抛出的异常信息，抛出异常信息为：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常。
#4）调用该方法提供的驱动程序作为参数，直到返回值为False，判断元素消失使用
# element=WebDriverWait(driver,30,1,(ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id("someId").is_displayed())
# print(element)
#判断元素EC(excepted_conditions)
# title_is： 判断当前页面的 title 是否完全等于（==）预期字符串，返回布尔值
# title=EC.title_is("百度一下，你就知道")
# print(title(driver)) #判断title与driver的title是否一致，一致为true
# title_contains : 判断当前页面的 title 是否包含预期字符串，返回布尔值
# title=EC.title_contains("百度一")
# print(title(driver)) #判断title与driver的title是否一致，一致为true
#以上两种方法简略写法
# r1=EC.title_contains("百度")(driver)
# r2=EC.title_is("百度一下，你就知道")(driver)
# print(r1,r2)
# presence_of_element_located : 判断某个元素是否被加到了 dom 树里，并不代表该元素一定可见

# visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于 0

# visibility_of : 跟上面的方法做一样的事情，只是上面的方法要传入 locator，这个方法直接传定位到的 element 就好了

# presence_of_all_elements_located : 判断是否至少有 1 个元素存在于 dom 树中。举个例子，如果页面上有 n 个元素的 class 都是'column-md-3'，那么只要有 1 个元素存在，这个方法就返回 True

# text_to_be_present_in_element : 判断某个元素中的 text 是否 包含 了预期的字符串

# text_to_be_present_in_element_value : 判断某个元素中的 value 属性是否包含了预期的字符串

# frame_to_be_available_and_switch_to_it : 判断该 frame 是否可以 switchtitle_is： 判断当前页面的 title 是否完全等于（==）预期字符串，返回布尔值

# title_contains : 判断当前页面的 title 是否包含预期字符串，返回布尔值

# presence_of_element_located : 判断某个元素是否被加到了 dom 树里，并不代表该元素一定可见

# visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于 0

# visibility_of : 跟上面的方法做一样的事情，只是上面的方法要传入 locator，这个方法直接传定位到的 element 就好了

# presence_of_all_elements_located : 判断是否至少有 1 个元素存在于 dom 树中。举个例子，如果页面上有 n 个元素的 class 都是'column-md-3'，那么只要有 1 个元素存在，这个方法就返回 True

# text_to_be_present_in_element : 判断某个元素中的 text 是否 包含 了预期的字符串

# text_to_be_present_in_element_value : 判断某个元素中的 value 属性是否包含 了预期的字符串

# frame_to_be_available_and_switch_to_it : 判断该 frame 是否可以 switch进去，如果可以的话，返回 True 并且 switch 进去，否则返回 False

# invisibility_of_element_located : 判断某个元素中是否不存在于 dom 树或不可见

# element_to_be_clickable : 判断某个元素中是否可见并且是 enable 的，这样的话才叫 clickable

# staleness_of : 等某个元素从 dom 树中移除，注意，这个方法也是返回 True或 False

# element_to_be_selected : 判断某个元素是否被选中了,一般用在下拉列表

# element_selection_state_to_be : 判断某个元素的选中状态是否符合预期

# element_located_selection_state_to_be : 跟上面的方法作用一样，只是上面的方法传入定位到的 element，而这个方法传入 locator

# alert_is_present : 判断页面上是否存在 alert

#判断文本text_to_be_present_in_element，locator 参数是定位的方法，locator 参数是定位的方法
# result=EC.text_to_be_present_in_element(("name","tj_trvirus"),"抗击肺炎")(driver)
# print(result)
#判断文本的value值text_to_be_present_in_element_value
# result=EC.text_to_be_present_in_element_value(("id","su"),"百度一下")(driver)
# print(result)

# 判断弹出框存在(alert_is_present)
#实例1：百度首页设置页面选择展示50页，然后返回保存结果的text
# mouse = WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "设置"))
# #移动鼠标至设置按钮
# ActionChains(driver).move_to_element(mouse).perform()
# #定时刷新等待后，点击搜索设置
# WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "搜索设置")).click()
# # 选择设置项
# s = WebDriverWait(driver, 10).until(lambda x: x.find_element("id", "nr"))
# #选择列表中的"每页显示 50 条"
# Select(s).select_by_visible_text("每页显示50条")
# 使用js点保存按钮
    #1.1js有5种定位，最后execute_script(js)来执行js，返回值为数组值，需要通过索引定位
    # document.getElementById(“id”)
    # document.getElementsByName(“Name”)
    # document.getElementsByTagName(“tag”)
    # document.getElementsByClassName(“class”)
    # document.querySelectorAll(“css selector")
    # 1.2浏览器滚动条的处理
    # js="var q=document.getElementById('id').scrollTop=0"           #滚动到顶部
    # js="var q=document.documentElement.scrollTop=10000"       #滚动到底部部
    # scrollTo(x, y）js ="window.scrollTo(100,400);"     #宽度为100，高度为400的位置
    # 1.3js点击（使用select模块时，会点击失效）
    # js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
    # driver.execute_script(js)
    # 1.4多窗口时，在当前页面打开窗口，处理方式同readonly属性的日历框处理
    # 跳转链接有 target="_blank" 属性，可以将此属性置空，然后再操作就不会打开新窗口
    # # 修改元素的 target 属性
    # js = 'document.getElementsByClassName("mnav")[0].target="";'
    # driver.execute_script(js)
# js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
# driver.execute_script(js)
# # 判断弹窗结果
# result = EC.alert_is_present()(driver)
# if result:
#     print(result.text)
#     result.accept()
# else:
#     print("alert 未弹出！")
#判断元素出现,出现则返回该元素
# result=EC.presence_of_element_located((By.ID,"su"))
# # 判断是否至少有 1 个元素存在于 dom 树中。举例：如果页面上有 n 个元素的 class 都是’wp’，那么只要有 1 个元素存在，这个方法就返回 True
# result1=EC.presence_of_all_elements_located(By.ID)
# print(result,result1)
#判断元素可见
result=EC.visibility_of_element_located((By.ID,'form'))
print(result(driver))

driver.refresh()
#退出浏览器进程
time.sleep(3)
driver.quit()