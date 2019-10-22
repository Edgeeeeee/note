# day05 
### 数据库连接 案例
- 见代码

### 异常处理
	异常是系统运行过程中出现的一系列问题的同城
	异常出现可能是用户的错误操作造成的，也可能是程序的确存在缺陷
	异常处理机制的目的是：
		1. 异常出现后给用户一些能够快速任职的解决和策略
		2. 当系统存在bug时，异常处理可以保证系统的其余功能还能正常工作。不至于导致系统完全崩溃
	Java中提供了一个顶层的可抛出的类用于系统向外发送错误信息Throwable，它有两个子类
		1. Error （系统错误）
		2. Exception （异常）
- 异常分类两类
	 - RuntimeException（运行时异常）
		 - 在编译期不检测，
	 - 编译期异常
		 - 会在编译过程中检测，如果不处理，程序将无法通过编译。

- 在方法中处理异常，保证方法通过编译的方式有两种
	- 主动的捕获
		- 使用try-catch-finally语句块捕获异常
	- 被动的声明
		- 在方法声名处使用throws关键字对异常类型进行声明


### Apache Tomcat
- 当今行业内最常用的应用服务器之一，可以在计算机上提供一个HTTP服务的应用
- 基本目录

		web Application Pro
			java Resources //所有的Java源代码（src目录）以及部分配置资源文件
			WebContent
				WEB—INF
					lib  // 包含项目所需的jar包
					web.xml  // web项目的基本配置文件
				css文件夹
				js文件夹
				img文件夹
				xxxx.html
### JSP
- JSP(java sever page) Java服务器页面
- jsp = html + Java脚本
- JSP的指令元素，JSTL（Java Standard TagLib），EL（Expression Language）
- 其他还需要了解的内容有：脚本元素，表达式元素，声明元素等等


##### get方式和post方式请求乱码解决
- get方式的请求中文乱码可以通过设置tomcat


### Servlet(web应用小程序）
- 用于接收客户端发送的请求
- 获取请求参数
- 相应客户端

# html表单标签
- 根标签 form
- input 输入框 按照type不同可能是文本框，密码框，单选按钮，复选按钮，
- select>option 下拉框
- button 按钮（普通按钮，提交按钮， 重置表单按钮）
- textarea 多行多列的输入框
		