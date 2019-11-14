# -*- coding:utf-8 -*-
# @Time     :2019/11/11 0011 16:33
# @Author   :Lemon_huahua
#@File      :spider02.py
#实现爬虫v2.0

import requests
from Spider.Spider999.spider01 import spider_v1          #程序头部引用
class spider_v2(spider_v1):                           #子类定义
    def __init__(self,url):                           #子类初始化参数
        self.url=url
        spider_v1.__init__(self)                      #必须在子类初始化中声明父类的初始化方法

if __name__=="__main__":
    url="https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

    spiderobj2=spider_v2(url)
    print(spiderobj2.zhuaqu(spiderobj2.url))