# -*- coding:utf-8 -*-
# @Time     :2019/11/11 0011 15:36
# @Author   :Lemon_huahua
#@File      :test.py
#面向过程
'''
a=3
b=4
s=a+b
print(s)
'''
#面向对象

'''
def addClass(a,b):
    s=a+b
    return s
print(addClass(2,3))
'''

'''
class addClass():               #定义一个类
    def __init__(self,a,b):     #初始化方法，定义类内部属性
        self.a1=a
        self.b1=b
    def add(self):              #定义其他方法
        s=self.a1+self.b1
        return s
    def plus(self):
        s=self.a1-self.b1
        return s

if __name__=="__main__":        #入口函数
    addobj=addClass(3,4)        #实例化对象
    sum=addobj.add()
    print(sum)
    plusobj=addClass(4,3)
    print(plusobj.plus())
'''
#
# from lxml import etree
# #定位内容
# document=etree.HTML('''<html>
# <p class="t1 ">
#             <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
#             <input class="checkbox" type="checkbox" name="delivery_jobid" value="118355173" jt="0" style="display:none" />
#             <span>
#                 <a target="_blank" title="软件测试工程师" href="https://jobs.51job.com/shanghai-pdxq/118355173.html?s=01&t=0"  onmousedown="">
#                     软件测试工程师                </a>
#             </span>
#                                                                     </p>
#         <span class="t2"><a target="_blank" title="上海优益基医疗器械有限公司" href="https://jobs.51job.com/all/co3145441.html">上海优益基医疗器械有限公司</a></span>
#         <span class="t3">上海-浦东新区</span>
#         <span class="t4">1-1.5万/月</span>
#         <span class="t5">11-12</span>
#
# </html>
# ''')
#
# for i in range(2,5):
#     ele=document.xpath('/html/body/span['+str(i)+']/text()')
#     print(ele)

# with open("1.txt",'a') as file:
#     # file.write("content")
#     file.writelines(["a","b"])


input()