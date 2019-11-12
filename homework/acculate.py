# -*- coding:utf-8 -*-
# @Time     :2019/11/12 0012 15:03
# @Author   :Lemon_huahua
#@File      :acculate.py
'''
#M与N的数学运算：用户输入两个数 M 和 N，其中 N 是整数，计算M 和 N 的5种数学运算结果，并依次输出，（编程题）
M=float(input ("M="))
N=int(input("N="))
print(M+N)
print(M-N)
print(M*N)
print(M/N)
print(M%N)
'''

#用户输入矩形的长和宽，计算其面积并输出
# chang=float(input("长:"))
# kuan=float(input("宽："))
# area=chang*kuan
# print(area)

'''
class area:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def cal_area(self):
        s=self.a*self.b
        return s
if __name__=="__main__":
    retangele_area=area(3,4)
    print(retangele_area.cal_area())
'''

#3位水仙花数计算：“3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。（编程题）

# for num in range(101,999):
#     i=num//100
#     j=num//10%10
#     h=num%10
#     if (i**3+j**3+h**3==num):
#         print (num)

#打印100以内的斐波那契数列（编程题）
# a=0
# b=1
# s=a+b
# while (s<100):
#     print(s)
#     a=b
#     b=s
#     s=a+b

#打印九九乘法表（编程题）
# for j in range(1,9):
#     for i in range(1,j+1):
#
#         print(i,'*',j,"=",i * j,'',sep='\t',end='')
#     print()


#计算1+2+3...+98+99+100 （编程题）

# s=0
# for i in range(1,101):
#     s=s+i
# print(s)

s=123
print(s/100)


