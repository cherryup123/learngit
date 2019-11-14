# -*- coding:utf-8 -*-
# @Time     :2019/11/11 0011 13:54
# @Author   :Lemon_huahua
#@File      :spider01.py
#实现爬虫v1.0，进行技术试验
'''
import requests
url="https://www.51job.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
response=requests.get(url,headers)
response.encoding="gbk"
print(response.text)
'''
#实现爬虫v1.0，抓取51testing首页信息
import requests
class spider_v1:                                        #普通类定义
    def __init__(self):                                 #子类初始化
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    def zhuaqu(self,url):
        response=requests.get(url,self.headers)
        response.encoding="gbk"
        return response.text

if __name__=="__main__":
    spiderobj=spider_v1()
    print(spiderobj.zhuaqu("https://www.51job.com"))
