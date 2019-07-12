# day02 上午html 
- html网页设计规则
	- 网页最外层的标签是<html>
	- 标签需要成对儿出现，包括开始标签和结束标签，有些结束标签是可选的，
	- 标签可以嵌套使用
	- 标签中可以定义属性，属性包含属性名和属性值，并且之间用等号分割，属性值一般用引号包含，如果属性值本身含有双引号，那就要用单引号。大小写不敏感，但是要使用小写属性
- html属性参考
	- class：定义一个或多个类名
	- id：定义唯一id
	- style：规定元素的行内样式
	- title：描述了元素的额外信息，作为工具条使用

- div:
	- div是块状元素的代表元素，功能是给网页分块，结合css技术给网页布局
- 列表:
	- 有序,无序,自定义 三种
	- 实际上不必考虑,在开发过程中,使用css改变样式,原有的样式都要去掉





# 下午Java
	日期类型的使用,日期和数值格式的处理
	关于Java中定义数组,以及部分集合框架api的使用
	关于java.io处理文件和文件内容读取,写入的问题

- 使用NumberFormat 处理数值格式
	- NumberFormat.getInstance()  000,000,000.000000格式
	- NumberFormat.getPersentInstance() 00%格式 省略掉小数点后面的位数
	- NumberFormat.getCurrencInstance(Locale.xx) $000,000,000.0000 根据locale.xx的不同,前面加上不同的符号
- 使用NumberDecimal 处理数值格式
	- static DecimalFormat xx = new DecimalFormat('###,###.####')
		- 表示整数三位用逗号分开,小数部分保留四位 
		- 若把#换成0,则小数部分不足4位的用0补齐

- 使用DateFormat实现不同格式输出日期
	- SimpelDateFormat('yyyy/MM/dd a hh:mm:ss')
	- 其中/可替换成汉字'年','月'和'-'
	- a 表示显示上午下午

- 数组
	- 两种定义方式.
	- 给出长度
	- 给出数组项


- 集合框架
	
		集合框架按照功能分类多种多样
		List,Set,Map
		List接口有多个典型的实现类
		底层使用顺序表实现的ArrayList(用于数据查询)
		底层使用链表实现的LinkedList(频繁的增删改操作)
		线程安全的List--Vector(多线程并发访问)

	- 创建List
		- List<obj> Name = new ArrayList<>(xx)
		- obj为为list指定范型,使list结点只能存储此class的实例
		- xx为容量
	- 添加:
		- list.add()
	- 删除:
		- list.remove(index/obj)
	- 修改:
		- list.set(index, value)
	- 查看:
		- list.get(index) 超范围报错
		- list.indexOf(obj) 没有返回-1

- 文件读写
	
		Java以数据流的方式对文件进行读取和写入
		流按照一次读写的类型可以分为:字节流和字符流
		字节流的读写以byte为单位,比较适合读写二进制文件
		字符流的读写以char为单位,比较适合用于顶文本文件
		字节流的两个顶级接口:InputStream和 OutputStream
		字符流的两个定义结构:Reader和Writer
	- 创建文件对象
		- File obj.name = new File("路径");
	- 创建一个读取指定文件的读取流
		- FileReader name = new FileReader(File);
	- 为读取流添加一个缓冲区(高效,方便)
		- BufferReader name = new BufferReader(FileReader);
	- 调用BufferReader中的方法读取文件
		- BufferReader.readline() 按行读取方法
	- 操作结束后,关闭io流
		- FileReader.close()
		- BufferReader.close()
	- 文件写入 则把所有的reader换成writer

- 心得

		今天是学习的第二天，老师为了调动学习的积极性，改变了教学的方法，第一天一直在学Java语法，今天上午学习了html语言基础，让我们对html语言有一个初步的认识，而我之前有过自己学习html，老师讲的知识我也很快就能理解，有了对html一个更系统的认识。下午继续学习Java，仍然是讲一些常用的语法，主要是一些常用的类和方法。学习过后，我了解了数值规范，日期处理，和文件读写的基本知识。