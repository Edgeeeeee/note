# 数据库恢复技术
- 事务的基本概念
	- 所谓事务时用户定义的一个数据库操作序列，这些操作要么全做，要么全不做，是一个不可分割的单位
	- 通常以begin transaction开始，以commit 或 rollback结束
	- commit 表示提交，即提交事务的所有操作，将对数据库的更新写回到磁盘上的物理数据库中去
	- rollback 表示回滚，系统将事务对数据库的所有已完成的操作全部撤销，回滚到事务开始时的状态
	- **事务的ACID特性**
		- **原子性**
			- 事务是数据库的逻辑工作单位，事务中包括的诸操作要么都做，要么都不做
		- **一致性**
			- 事务执行的结果必须是使数据库从一个一致性状态变到另一个一致性状态，当数据库只包含成功事务提交的结果时，就说数据库处于一致状态，如果发生故障，一个未完成事务的一部分修改进入数据库，这时数据库就处于一种不正确的状态
		- **隔离性**
			- 一个事务的执行不能被其他事务干扰，即事务内部的操作和使用数据对其他并发事务是隔离的，并发执行的各事务之间不能干扰
		- **持续性**
			- 也称为**永久性**，指事务一旦提交，他对数据库的改变就是永久的。接下来的操作和故障不该对其结果有任何影响
- 故障的种类
	- 事务内部的故障
		- 事务内部更多的故障时非预期的，是不能由应用程序处理的。如运算溢出，并发事务死锁等，事务故障仅指这些非预期的故障
		- 这类事务内的恢复操作位称为事务撤销
	- 系统故障
		- 系统故障是指造成系统停止运转的任何事件，使得系统要重新启动。这类故障影响正在运行的事务，但不破坏数据库。
		- 发生系统故障时，一些尚未完成的事务的结果可能已经送入数据库，从而造成数据库可能处于不正确的状态
		- 恢复子系统必须在系统重新启动时让所有非正常中止的事务回滚，强制撤销所有未完成的事务
		- 除了撤销未完成的事务之外，还需要**重做**已撤销的事务，以将数据恢复到一致状态
	- 介质故障
		- 系统故障称为**软故障**，介质故障则称为**硬故障**，可能性较小，但破坏性最大
	- 计算机病毒
		- 数据库本身被破坏
		- 数据不正确
- **恢复原理**：**冗余**
- 恢复的实现技术
	- 建立冗余数据最常用的技术是数据转储和登记日志文件，通常在一个数据库系统中，两种方法是一起使用的
	- 数据转储
		- 数据转储指管理员定期的将整个数据库复制到其他介质保存起来的过程，这些备用的数据称为后备副本
		- 重装后备副本只能将数据库恢复到转储时候的状态。
		- 静态转储
			- 在系统中无运行事务时进行的转储操作
		- 动态转储
			- 转储期间允许对数据库进行存取或修改
		- 海量转储
			- 一次转储所有的数据
		- 增量转储
			- 每次只转储更改的数据
		- 转出分类
			- 动态海量转储
			- 动态增量转储
			- 静态海量转储
			- 静态增量转储
	- 登记日志文件
		- 日志文件是用来记录事务对数据库更新操作的文件
			- 以记录为单位的日志文件
			- 以数据块为单位的数据文件
		- **日志文件需要登记的内容包括**：
			- 各个事务的开始
			- 各个事务的结束
			- 各个事务的所有更新操作
		- **每个日志记录的内容主要包括：**
			- 事务标识
			- 操作的类型
			- 操作对象
			- 更新前数据的旧值
			- 更新后数据的新值
		- 日志文件的作用
			- 事务故障恢复和系统故障恢复必须用日志文件
			- 在动态转储时必须建立日志文件
			- 在静态转储时也可以建立日志文件
		- **登记日志文件必须遵循的两条原则：**
			- 登记的次序严格按照并发事务执行时间的次序
			- 必须先写日志文件，后写数据库
- 恢复策略
	- 事务故障恢复步骤
		- 反向扫描日志文件
		- 对该事务更新的操作执行逆操作
		- 继续扫描日志文件
		- 直至读到此事务的开始标记
	- 系统故障的恢复步骤
		- 正向扫描日志文件，找出故障发生以前已经提交的事务，将这些事务标记入重做队列。同时找出故障发生时尚未完成的任务，将其事务标记入撤销队列
		- 对撤销队列中的事务进行撤销处理
			- 撤销的处理方法是：反向扫描日志文件，对每个撤销事物的更新操作执行逆操作，即将日志中更新前的值写入数据库
		- 对重做队列中的各个事务进行重做处理
			- 进行重做处理的方式：正向扫描日志文件，对每个重做事务重新执行日志文件登记的操作，即将日志记录更新后的值写入数据库
	- 介质故障的恢复
		- 最严重的故障，恢复方法是重装数据库，然后重做已经完成的事务
			- 装入最新的数据库后被副本，对于动态转储的数据库副本，还应该装入转储开始时刻的日志文件副本
			- 转入相应的日志文件副本(转储结束后的日志)重做已经完成的事务