# day01 数据类型，字符串，日期类型
- 包的命名原则
	- 域名倒序
	- 小写字母
	- 点分割
- 类的命名规则
	- 大驼峰
- 数据类型分为两大类
	- 基本数据类型
	- 引用类型
		- Java中除了八种基本数据类型外都是引用类型
- 基本数据类型（8种）
	- 数字:short，int（整数默认为int），long，float（以f或F结尾），double（浮点数默认为double型）
	- 字符:char(两个字节)
	- 字节：byte（一个字节）
	- boolean	
		- 实际上在Java编译器中 一个布尔类型是以整形来表示的
		- 但是一个boolean类型的数组使用byte型表示的
- java 语言自负的默认编码是国际统一编码unicode
- Java语言所有的类型都直接或者简介继承字object类

- 为了方便编程，Java语言的开发者为八种基本数据类型提供了八个包装器类型，他们都是引用类型
	- short -> Short
	- long -> Long
	- float -> Float
	- double -> Double
	- boolean -> Boolean
	- byte - Byte
	- int -> Integer
	- char -> Character
- 自动装箱：自动将基本数据类型转换成包装器类型

		int a = 10;
		Integer b = a, c = new Integer(a);
		// a是int型 b，c为Integer包装器类型

- 自动拆箱:自动将包装类型转换成基本数据类型的机制

		Boolean b21 = new Boolean(false);
		bollean b22 = b21, b23 = b21.booleanValue();
		//b21是Boolean包装器类型，b22,b23是bollean类型。

- 字符串
	- 常量不变性
		- 基于字符串的所有操作都不会将原来的字符串修改
		- 存放在新的存储空间中
		- 在字符串的操作中会产生内存浪费，而且回收不及时，效率不高。
		- System.out.println("a"+"b"+"c"+"d");会产生"a","b","c","d","ab","abc"六个垃圾内存
		- 解决办法
			- 提供了两个引用类型StringBuffer和StringBuilder,使用方法和String基本相同
			- StringBuilder：并发不安全，但是运行快。
			- StringBuffer：并发安全。
	- 拼接：用String.concat或者加号"+"实现
	- 截取：String.substring(a[,b]) 参数为字符串索引，左闭右开，可以省略第二个参数，表示直到结束
	- 查找：
		- 给定字符（串）查找索引，没有返回-1 String.indexOf()
		- 给定索引，返回指定位置的字符，超出范围报错 String.charAt()
	- 替换：String.replace()
	- 删除：String.delete(a,b) 删除指定区间的内容
	- 反转：String.reverse



- 心得

		第一天实习，也是第一次实习，以为会很严肃，就像是上班了一样。但实际上还是挺轻松的，学习氛围很好。老师也很为我们着想，在了解我们是第一次接触Java后，老师讲的很详细，很轻松就能听懂，了解了很多知识。经过了一天的学习，对Java有一个初步的了解。知道了基本语法，实际上Java和c++有很多的相似之处，在学过c++的基础上在学Java要轻松很多