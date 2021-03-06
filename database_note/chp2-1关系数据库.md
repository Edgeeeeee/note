# 第二章 关系数据库
## 关系数据结构及形式化定义
- 关系
	- D1 X D2 X D3... X Dn的__子集__叫做在域D1,D2,D3... Dn上的__关系__
	- 表示为R(D1,D2,D3...Dn)
	- R 为关系名
	- n 为关系的__目__或__度__
		- n = 1 时为 一元/单元 关系
		- n = 2 时为二元关系
- 元组
	- 关系中每个元素是关系中的元组，通常用t表示
- 关系的表示
	- 关系也是一个二维表，表的每行对应一个元组，表的每列对应一个域
- 属性
	- 关系中不同的列可以对应相同的域
	- 为了加以区分，必须对每列起一个名字，称为属性
	- n 目关系必须有 n 个属性
- 码
	- __候选码__
		- 若关系中的某一属性组的值能唯一标识一个元组，则称该属性组为候选码
	- __全码__
		- 最极端的情况：关系模式的所有属性组是这个关系模式的候选码
	- __主码__
		- 若一个关系有多个候选码，则选定其中一个为主码
	- __主属性__
		- 候选码的所有属性都为主属性
		- 不包含在任何候选码中的属性称为非主属性 或 非码属性
- 三类关系
	- 基本关系
		- 实际存在的表，是实际存储数据的逻辑表示
	- 查询表
		- 查询结果对应的表
	- 视图表
		- 由基本表或其他视图表导出的表，是虚表，不对应实际存储的数据
- 关系模式
	- 对关系的描述
	- 静态的，稳定的
- 关系
	- 关系模式在某一时刻的状态和内容
	- 动态的，随时间不断变化的
	- 关系模式和关系往往统称为关系，通过上下文加以区别
- 关系数据库
	- 关系数据库的**型**与**值**
		- **关系数据库的型**：关系数据库模式，对关系数据库的描述
		- **关系数据库模式包括**
			- 若干域的定义
			- 在这些域上定义的若干关系模式
		- **关系数据库的值**：
			- 关系模式在某一时刻对应的关系的集合，简称为关系数据库
- 关系操作的特点
	- 集合操作方式：操作的对象和结果都是集合
- 关系的完整性
	- 实体完整性和参照完整性是关系模型必须满足的两个完整性约束条件，称为关系的两个不变性，应该由关系系统自动支持
	- 实体完整性
		- 若属性A是基本关系R的主属性，则属性A不能取空值
	- 参照完整性
		- 外码
			- 设F是基本关系R的一个或一组属性，当不是关系R的码。如果F与基本关系S的主码Ks相对应，则称F是基本关系R的**外码**
			- 基本关系R称为**参照关系**
			- 基本关系S称为**被参照关系**或**目标关系**
			- 注意：
				- 关系R和S不一定是不同的关系
				- 目标关系S的主码Ks和参照关系的外码F必须定义在同一个(或一组)域上
				- 外码不一定要与相应的主码同名，当外码与相应的主码属于不同关系时，往往取相同的名字以便识别
		- 参照完整性规则
				- 或者取空值（F的每个属性均为空值）
				- 或者等于S中某个元组的主码值
	- 用户定义完整性
		- 针对某一个具体关系数据库的约束条件，反应某一具体应用所涉及的数据必须满足的语义要求