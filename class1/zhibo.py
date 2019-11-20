#python 网易云音乐 登录接口
#https get post
#soap xml post

import requests
import json
class RunMain:


    def send_post(self,url,data):

        response=requests.post(url,data=data).json()
        res=json.dumps(response,sort_keys=True,indent=2)
        return res
if __name__ == '__main__':
    url=
    runmainobj=RunMain()
    runmainobj.send_post(url)

