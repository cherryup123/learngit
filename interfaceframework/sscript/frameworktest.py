#通过unittest框架实现多个接口的联调测试（注册和登录接口）
import unittest2
import requests
class mulinterface_test(unittest2.TestCase):
    def setUp(self):
        print("setUp")
    def test_login(self):
        print("登录接口")
    def test_register(self):
        print("注册接口")
    def tearDown(self):
        print("tearDown")
if __name__ == '__main__':
    #声明测试套对象
    suite=unittest2.TestSuite()
    suite.addTest(mulinterface_test("test_case2"))
    #声明测试运行对象
    runner=unittest2.TextTestRunner()
    runner.run(suite)

    # unittest2.main()


#实验2：针对检查接口通过unittest框架进行脚本实现
# import unittest2
# import requests
# import csv
#
# class testcheck(unittest2.TestCase):
#     def setUp(self):
#         self.url = "http://localhost:8080/jwshoplogin/user/check_vaild.do"
#         self.file1 = open("checkuseremaiinfo.csv", 'r')
#         self.file2 = open("checkresult.csv", "w")
#     def test_check(self):
#         check_info = {}
#         data = csv.reader(self.file1)
#         for row in data:
#             check_info["str"] = row[0]
#             check_info["type"] = row[1]
#             s = requests.session()
#             response = s.post(self.url, data=check_info).text
#             # 通过assert函数进行测试结果的判断
#             self.assertIn(row[2],response)
#     def tearDown(self):
#         self.file1.close()
#         self.file2.close()
# if __name__ == '__main__':
#     unittest2.main()



 # #实验1：使用unittest框架进行注册接口测试
# import unittest2
# import requests
# class testregister(unittest2.TestCase):
#     def setUp(self):
#         self.url = "http://localhost:8080/jwshoplogin/user/register.do"
#         self.userinfo = {}
#         self.userinfo = {"username": "cc", "password": "111111",
#                          "email": "cc@qq.com", "phone": "13111111111",
#                          "question": "喜欢的书", "answer": "三国演义"}
#     def test_register(self):
#         s=requests.session()
#         response=s.post(self.url,data=self.userinfo).json()
#         self.assertIn("用户名已经存在",str(response))
# if __name__ == '__main__':
#     unittest2.main()