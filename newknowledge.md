


#鼠标操作
ActionChains(driver).double_click(element).perform()  双击
ActionChains(driver).context_click().perform()        右击

#frame  使用frame的name定位
driver.switch_to.frame("mainFrame")  

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

#css定位
1.多个class  driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
2.任意属性定位 driver.find_element_by_css_selector("[value*='1']").click() 
3.id 定位  #   父子关系>  祖先关系  空格  *= 包含 ^=开头 $=结尾

#等待
1.driver.implicitly(5)  隐式等待  智能等待，自动判断等待时间 程序开始处写一次 页面加载
2.time.sleep(5)         处理弹出框
3.WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present()) 
 显示等待，满足条件后才不等待
  from selenium.webdriver.support.wait import WebDriverWait
  from selenium.webdriver.support import expected_conditions

#窗口
1.最大化  driver.maximize_window()
2.窗口切换   new_window=driver.window_handles[-1]   driver.switch_to.window(new_window)

#下拉框
1.定位   element=driver.find_element(...)
2.将页面元素转换成Select类
Select(element).select_by_value('选项的value属性值')
Select(element).select_by_index(第几个选项)
Select(element).select_by_visible_text("选项的文本值")

#操作日历控件  JS
script='document.getElementById("date").removeAttribute("readonly")'  删除readonly属性
driver.execute_script(script)

#弹窗 alert
driver.switch_to.alert.accept()    确定
driver.switch_to.alert.dismiss()   取消
driver.switch_to.alert.text        文本

#.上传文件和图片   <input ...>
定位到元素+send_key("文件路径")

#submit()  提交表单  只能用于form表单中
driver.find_element_by_id("password").submit()

**********************************python基础**********************************
#抓取页面信息 发送请求 得到回应
import requests
url="https://www.51job.com/"
headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
response=requests.get(url,headers)
response.encoding="gbk"   #中文页面出现乱码时
print(response.text)

#提取html文件中的内容
from lxml import etree
document=etree.HTML('''<html lang="en"><body><p>123</p></body></html>''')#定位
content=document.xpath("/html/body/p/text()")    #定位元素并读取内容  @title
print(content)

#将内容保存在txt文件中
path=r"D:\learngit\web_auto\SeleniumTest2\func\1.txt"
with open(path,'a') as file:          #a 是追加 w 是清空再写入 r 只读
    file.write("content")             #写入字符串
    file.writelines(["2","4"])       #写入多个字符串，列表形式
    
#读取csv文件内容
import csv
import os
base_path=os.path.dirname(__file__)
file_path=base_path+'/userinfo.csv'
print(file_path)
file=open(file_path)
data=csv.reader(file)
for row in data:
    print(row)
    
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