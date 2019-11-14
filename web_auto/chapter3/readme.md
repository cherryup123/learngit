总结
1.隐式等待
driver.implicitly(5)  智能等待，自动判断等待时间 程序开始处写一次 页面加载
time.sleep(5)         处理弹出框
显示等待  满足条件后才不等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present())

2.窗口最大化
driver.maximize_window()
3.窗口切换
new_window=driver.window_handles[-1]
driver.switch_to.window(new_window)

4.下拉框选择
from selenium.webdriver.support.select import Select
4.1定位下拉框
element=driver.find_element(...)
4.2将页面元素转换成Select类
Select(element).select_by_value('选项的value属性值')
Select(element).select_by_index(第几个选项)
Select(element).select_by_visible_text("选项的文本值")
5.定位一组元素
find_elements

1.本次工作任务：个人信息修改
2.任务分解

技术学习
1.submit()  提交表单  只能用于form表单中
driver.find_element_by_id("password").submit()
2.css_selector定位
driver.find_element_by_css_selector("[value='1']").click() [任意属性定位]
class属性定位 .  id属性定位     #父子关系>  祖先关系  空格

3.如何操作日历控件  删除readonly属性  JS
script='document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(script)

4.弹出框处理 alert
driver.switch_to.alert.accept()    确定
driver.switch_to.alert.dismiss()   取消
driver.switch_to.alert.text        文本

5.上传文件和图片   <input ...>
定位到元素+send_key("文件路径")



