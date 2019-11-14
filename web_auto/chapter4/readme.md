1.验证码处理方式
1）第三方图片文字识别
2）第三方网站识别
3）万能验证码
4）内网ip地址屏蔽验证码
5）读取cookie和缓存
6）等待时间+手动点击

如何查看开发是否设置了万能验证码？
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

2.frame  使用frame的name定位
driver.switch_to.frame("mainFrame")    

3.鼠标操作
ActionChains(driver).double_click(element).perform()  双击
ActionChains(driver).context_click().perform()        右击
ActionChains(driver).double_click().perform()         
ActionChains(driver).double_click(element).perform()  
ActionChains(driver).double_click(element).perform()  

4.