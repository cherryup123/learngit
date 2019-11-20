#技术点（针对web自动化测试）

#窗口切换
1.找到新窗口的名字
2.切换到新窗口
new_window=driver.window_handles[-1]
driver.switch_to.window(new_window)
all_handles=driver.window_handles                #获取所有句柄
current_window=driver.current_window_handle      #获取当前句柄
#窗口控制
driver.maximize_window()
driver.set_window_size(width=400,height=800)
driver.forward()
driver.back()
driver.refresh()  #刷新页面
title=driver.title             #获取页面标题
url=driver.current_url         #获取页面URL
driver.save_screenshot("截图存放地址.png")    #截图
#元素操作
size=driver.find_element_by_id("su").size         #返回元素大小
text=driver.find_element_by_id("su").text         #返回文本信息
attribute=driver.find_element_by_id("su").get_attribute("class")  #获取其他属性
result=driver.find_element_by_id("su").is_displayed()        #元素是否可见
#鼠标操作
from selenium.webdriver import ActionChains
ActionChains(driver).context_click(element).perform()    #右击
ActionChains(driver).move_to_element(element).perform()  #鼠标悬浮
ActionChains(driver).double_click(element).perform()     #双击
ActionChains(driver).drag_and_drop(element1,element2).perform()    #拖动
#滑动解锁
slider=driver.find_element_by_id("slide")               #定位到滑块   
ActionChains(driver).click_and_hold(slider).perform()   #按住滑块    
for i in range(200):                                             
    ActionChains(driver).move_by_offset(2,0)       #移动鼠标,x,y坐标   
    ActionChains(driver).reset_actions()           #重置action     
#滑动日历  TouchActions                                                               
element=driver.find_element_by_id("year")          #定位到元素             
action=webdriver.TouchActions(driver)                                 
action.scroll_from_element(element,0,5).perform()  #滑动鼠标 x,y坐标        
#键盘操作
from selenium.webdriver.common.keys import Keys
driver.find_element_by_id("su").send_keys(Keys.CONTROL,'a')
driver.find_element_by_id("su").send_keys(Keys.BACK_SPACE)  #删除键
driver.find_element_by_id("su").send_keys(Keys.F1)          #F1键
#下拉框
from selenium.webdriver.support.select import Select
element=driver.find_element_by_id("su")
Select(element).select_by_value(value="20")           #通过value值定位
Select(element).select_by_index(0)                    #通过索引定位
Select(element).select_by_visible_text("下拉选项的值")#通过text定位
#文件路径
file_path1=os.path.dirname(__file__)+'/userinfo.csv'
#文件下载
options=webdriver.ChromeOptions()
prefs={"profile.default_content_settings.pops":0,  #不弹窗
       "download.default_directory":os.getcwd()} 
options.add_experimental_option("pref",prefs)
driver=webdriver.Chrome(chrome_options=options)
#js调用   操控日历控件
js="window.scrollTo(100,200);"   #控制浏览器滚动条位置
js="document.getElementById("id").value='"+input_text+"';"
script='document.getElementById("date").removeAttribute("readonly")'  删除readonly属性
driver.execute_script(script)
#调用js内置对象arguments处理视频播放HTML5                                                    
video=driver.find_element_by_id("preview-player_html5_api")                      
url=driver.execute_script("return arguments[0].currentSrc;",video) #返回视频的URL     
driver.execute_script("arguments[0].play()",video)                #播放视频          
driver.execute_script("arguments[0].pause()",video)                              
driver.execute_script("arguments[0].load()",video)                               
#内嵌页面
driver.switch_to.frame("mainFrame")    #id 或name可以直接跳转否则先找到元素
driver.switch_to.default_content()     #回到最外层页面
#警告框
alert=driver.switch_to.alert()
alert.text                  #获取警告框提示信息
alert.dismiss()             #拒绝
alert.accept()              #接受
alert.send_keys("输入文本") #输入文本信息
#xpath定位
driver.find_element_by_xpath('//*[@id="su" and @class="s_ipt"]') #属性定位
driver.find_element_by_xpath("//span[contains(@class,'s_ipt')]/input") #匹配属性字符串
driver.find_element_by_xpath("//a[text(),'新闻']")             #匹配文本
driver.find_element_by_xpath("//a[contains(text(),'新闻')]")
#css selector 定位
1.多个class  driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
2.任意属性定位 driver.find_element_by_css_selector("[value*='1']").click() 
3.id 定位  #   父子关系>  祖先关系  空格  *= 包含 ^=开头 $=结尾

#输出
print("age is %d,name is %s"%(age,name))
print("age is",age,"name is",name)
print("age is {},name is {}".format(age,name))
#列表(数组)
list_a=[1,2,3,4,'a']
list_a.append(2)   #列表末尾添加元素
list_a.pop(0)      #输出元素
#字典
dict_a={"age":22,"name":"tom"}
for key,value in dict_a.items():
    print(key,value)
dict_a.pop("age")  #删除键值对

#时间等待(脚本稳定性)
1.time.sleep(3)          处理弹出框
2.driver.implicitly(5)   
隐式等待  智能等待，自动判断等待时间 程序开始处写一次 页面加载
3.WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present()) 
显示等待，满足条件后才不等待
  from selenium.webdriver.support.wait import WebDriverWait
  from selenium.webdriver.support import expected_conditions
 
 #查找万能验证码
验证码处理方式
1）第三方图片文字识别
2）第三方网站识别
3）万能验证码
4）内网ip地址屏蔽验证码
5）读取cookie和缓存
6）等待时间+手动点击

1.确认开发源代码位置            MVC 设计模式  
M：Model 与数据库相关，包含表和类（实例）
V:View  主要和前端界面有关，用于收集和显示用户数据
C:Controller   业务逻辑
是否设置验证码属于业务逻辑
2.分析网址 
url="http://127.0.0.1/index.php?m=user&c=public&a=login"
协议+ip/域名（端口号）+路径+参数
m=user&c=public&a=login  
user包publiccontroller文件名login action方法
strtolower(I('userverify')) != '1234'
#python操作数据库
import mysql.connector
db=mysql.connector.connect(user='root',password='123456',database="test",charset="utf8")
cursor=db.cursor() #获取操作游标
sql='insert  into human4 VALUES ("ming","li","23","2900")'  #插入数据
cursor.execute(sql)  #执行SQL语句
db.commit()  #提交到数据库执行
db.close() 
sql='''create table human4(first_name char(20) not null,  #创建表
last_name char(20),age int,income float)'''
sql='select * from human4 where income >%r' %(1000)  #查询表
results=cursor.fetchall()
for row in results:
    fname=row[0]
    lname=row[2]
    age=row[3]
    income=row[4]
    print("fname=%s,lname=%s,age=%s,income=%s"%(fname,lname,age,income))
db.rollback()  #回滚数据
#读取txt
with open("test.txt",'r') as file:                                                                     
    data=file.readlines()       #read读取整个文件str readline读取一行 readlines读取多行列表                                                                                                       
    users=[]                                                                                           
    for line in data:                                                                                  
        user=line[:-1].split(':')    #split对字符串进行拆分成数组                                                 
        users.append(user)    
#读取csv                                                                         
import csv                                                       
with open("data.csv","r") as file:                               
    data=csv.reader(file)                                        
    i=0                                                          
    for row in data:                                             
        if(i>0) :              #去除首行                             
            print(row)                                           
        i=i+1                                                    
#读取xml文件                                                          
from xml.dom.minidom import parse                                 
dom=parse("xml文件.xml")    #打开文件                                   
root=dom.documentElement     #获取页面所有元素                            
tag_name=root.getElementsByTagName('login')      #找到标签login       
username=tag_name[0].getAttribute("username")    #找到属性username的值 
#提取html文件中的内容
from lxml import etree
document=etree.HTML('''<html lang="en"><body><p>123</p></body></html>''')#定位
content=document.xpath("/html/body/p/text()")    #定位元素并读取内容  @title
print(content) 
#读取json文件                                                 
with open("test.json","r") as file:                       
    data=file.read()                                      
user_list=json.loads(data)                                
print(user_list)       
if __name__ == '__main__':                                                                                     
    suite=unittest2.TestSuite()            #创建测试套件                                                             
    suite.addTest(TestCalculator("testadd"))                                                                   
    runner= unittest2.TextTestRunner()    #创建测试运行器                                                             
    runner.run(suite)                                                                                          
                                                                                                               
    suite=unittest2.defaultTestLoader.discover("./TestCase","*Test.py")                                        
    runner= unittest2.TextTestRunner()    #创建测试运行器                                                             
    runner.run(suite)                                                                                          
                                                                                                               
    suite=unittest2.defaultTestLoader.discover("./TestCase","*Test.py")                                        
    runner= HTMLTestRunner(stream="存放的文件",title="报告名",description="测试环境",tester="changcheng")  #创建测试运行器                                                                                                                     
                                   
         