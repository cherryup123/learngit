# -*- coding:utf-8 -*-
# @Time     :2019/11/12 0012 9:41
# @Author   :Lemon_huahua
#@File      :spider03.py
import requests
from lxml import etree
from Spider.Spider.spider02 import spider_v2

class spider_v3(spider_v2):
    def __init__(self):
        spider_v2.__init__(self,url)
    def postion(self,htmltext):
        dic={}
        document=etree.HTML(htmltext)
        ele=document.xpath('//*[@id="resultList"]/div[10]/span[1]/a/text()')
        dic['公司名称']=ele
        return dic
    def savadata(self,content):
        with open('company.txt','w') as file:
            file.writelines(str(content))

if __name__=='__main__':
    url='https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    spiobj3=spider_v3()
    spiobj3.url=url
    res=spiobj3.zhuaqu(spiobj3.url)
    pos=spiobj3.postion(res)
    print(pos)
    spiobj3.savadata(pos)





