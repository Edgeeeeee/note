# MVC
	Model：模型（业务逻辑层Service/数据访问层DAO/实体类Entity）
	View：视图（HTML/CSS/JavaScript/ajax/jsp/模板技术）
	Controller：控制器（Servlet/Strust1~2/SpringMVC/EJB1~3）

- Entity：
	- 一般用于封装数据表信息，可以粗略地认为系统中每一个数据库表（中间表例外）都应该有一个实体类与其对应，表的每一个字段都对应实体类的一个成员变量（属性）

- JavaBean
	- 泛指符合以下特征的Java类的统称
		- 共有的类
		- 私有属性
		- 必须定义一个空参的构造方法
		- 为每一个私有属性提供一对getter和setter方法

- DAO层
	- 数据访问层，泛指一切用于数据访问的类和接口。

- JSTL(java standard taglib)
	- 提供了大量的标准化标签，赋予了jsp页面结构化获取模型数据和渲染视图的能力

- EL(Expression Language)
	- 可以更加方便地从视图对象中获取到模型数据