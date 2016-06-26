from splinter.browser import Browser
from splinter import Browser
import time
import traceback

#设定用户名和密码
username = u"595890662@qq.com"
passwd = u""

#起始地址的cookies值要自己去找, 下面两个分别是上海, 武汉
fromStation = u"%u4E0A%u6D77%2CSHH"
toStation = u"u5E7F%u5DDE%2CGZQ"

#时间格式2016-06-30
dtime = u"2016-06-30"
#车次，选择第几趟，0从上往下依次点击
order = 0
#设定乘客姓名
pa = u"王成志"

#网址
ticket_url = u"https://kyfw.12306.cn/otn/lcxxcx/init"
login_url = u"https://kyfw.12306.cn/otn/login/init"
initmy_url = u"https://kyfw.12306.cn/otn/index/initMy12306"

#登录网站
def login():
    b.find_by_text(u"登录").click()
    time.sleep(3)


#使用splinter打开chrome浏览器

executable_path = {'executable_path': '<C:\Program Files (x86)\Google\Chrome\Application\chrome.exe>'}
global b
b = Browser('chrome', **executable_path)

login()










