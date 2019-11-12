总结
1.隐式等待
driver.implicitly(5)  智能等待，自动判断等待时间 程序开始处写一次 
time.sleep(5)

2.窗口最大化
driver.maximize_window()
3.窗口切换
new_window=driver.window_handles(-1)
driver.switch_to.window(new_window)
4.下拉框选择
from selenium.webdriver.support.select import Select
定位下拉框
element=driver.find_element(...)
将元素转换成Select类型
Select(element).select_by_value('选项的value属性值')
Select(element).select_by_index(第几个选项)
Select(element).select_by_visible_text("选项的文本值")
5.定位一组元素
find_elements