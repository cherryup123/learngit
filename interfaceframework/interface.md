需求：通过unittest框架实现注册接口的测试
设计：
1.导入unittest类库
2.定义测试类 必须继承unittest类  
3.测试方法必须以test_开头，多个方法按照asc码顺序运行 
4.在main函数中使用unittest.main()
5.加入测试断言  self.assertIn("用户名已经存在",str(response))
6.通过setup进行初始化   每个方法都会执行一次
7.使用teardown进行测试的回收工作  每个方法都会执行一次
8.使用测试套进行测试用例的执行 
声明测试套件
需要执行的测试用例方法加入测试套件中
声明框架运行的对象
通过runner对象执行测试套件

