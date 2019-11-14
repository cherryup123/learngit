#抓取页面信息 发送请求 得到回应
import requests
url="https://www.51job.com/"
headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
response=requests.get(url,headers)
response.encoding="gbk"   #中文页面出现乱码时
print(response.text)