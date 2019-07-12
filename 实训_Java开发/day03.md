# 第三天 上午 css
	css:级联样式表
- 标签样式的添加位置
	- 添加在标签的style中，内嵌样式，优先级最高
	- 添加在head内的style标签中， 内联样式
	- 添加在外部css文件，外两样式
		- 外联样式需要用link标签引用
- 选择器
	- 用于指定样式需要作用于那些元素
	- 常用选择器包括
		- 元素选择器
		- id选择器
		- 类选择器
			- 类名第一个字符不能为数字
		- 父选择器
			- div p{}
			- 选中div下的直接的p元素
		- 子选择器
			- div > p{}
			- 选择div下所有的p元素
		- 派生选择器
	- 特殊选择器
		- 伪类选择器：只有在满足条件时候才会生效
			- ：hover 悬停
			- ：nth-child(n) 表示第n个子元素
		- 伪元素选择器
	- 选择器可以并用，选择更精确

			div .box1{}
			表示 div元素 并且 使用box1类

	- *：表示选择网页中的所有元素，在开发中有唯一的一个用途
		- 去除所有元素默认的边距
		- *{margin：0px；padding：0px；}

- css中常用的样式
	- 字体：
		- font
		- font-size
		- font-weight
		- font-family
		- font-style
	- 颜色
		- 
	- 背景
	- 边框
		- border-color
		- border-width:宽度
		- border-radius()
		- border-stylle
	- 浮动
	- 定位
		- position
		- 相对定位：relative
			- 元素相对于它原来的位置，以一个方向为基准，向反方向移动距离。
		- 绝对定位：absolute
		- 混合定位：fixed