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