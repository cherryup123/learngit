测试开发之路
1.语言基础Python
2.web自动化
3.接口测试
4.性能
5.手机自动化

快速突破开发瓶颈
1.编程思想
需求分析  程序设计流程图 代码实现 程序调试
要求：语法熟练 脚本设计及开发能力 测试框架设计及开发 测试工具设计研发
2.算法分析及实现
3.项目迭代
4.触类旁通




启动时间
cup 内存使用
FPS 每秒传输速度
流量
GPU

手工性能测试（adb命令）
获取app
adb logcat|findstr START
包名 com.android.browser

活动名/.BrowserActivity
启动命令 adb shell am start -w -n com.android.browser/.BrowserActivity
ThisTime:1485
冷热启动命令
冷启动 一个结束的app打开所消耗的时间
热启动 从后台运行重新到前端的时间

关闭命令不一样
冷启动关闭  adb shell am force-stop 包名
热启动关闭  adb shell input keyevent 3 按下了home键

产品经理 竞品 历史产品 
自动化性能测试
