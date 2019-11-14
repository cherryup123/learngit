#技术实验
#提取html文件中的内容
from lxml import etree
document=etree.HTML('''<html lang="en"><body><p>123</p></body></html>''')#定位
content=document.xpath("/html/body/p/text()")    #读取内容
print(content)

#抓取页面信息
# import requests
# url="https://www.51job.com/"
# headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
# response=requests.get(url,headers)
# response.encoding="gbk"   #中文页面出现乱码时
# print(response.text)