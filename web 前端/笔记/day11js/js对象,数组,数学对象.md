# js对象

```
1.使用原始的方式创建内置对象
    var myObject = new Object();
    myObject.name = “lijie”;
    myObject.age = 20;
    myObject.say = function(){...}

2.直接创建自定义对象
    var 对象名 = {属性名1：属性值，属性名2：属性值2，…….}

*3.使用自定义构造函数创建对象
    function pen(name,color,price){
        //对象的name属性
        this.name = name;
        //对象的color属性
        this.color = color;
        //对象的piece属性
        this.price = price;
        //对象的say方法
        this.say = function(){};
    }

    var pen = new pen(“铅笔”,”红色”,20);
    pen.say();

```

## this关键字

```
this单词本身就是  这个 的意思
在对象的方法中使用,代表着当前这个对象
意味着当对象调用这个方法时,方法中的this就代表着这个对象

```

## 遍历

```
for(var i in window){
    document.write(i+”----”+window[i]);
}
这种语句可以遍历对象中的所有属性或数组中的所有元素。

```

## 关于类型

```
测试类型:
1.typeof()  //global对象的其中一个方法，typeof()
2.对象.constructor; //查看当前对象的构造函数是谁

if(arr.constructor==Array){
    alert("数组"); //数组推荐用这种方法，因为typeof得到是object
}
```

# js数组

数组就是一组数据的集合，javascript中，数组里面的数据可以是不同类型的。

**定义数组的方法**

```
//对象的实例创建
var aList = new Array(1,2,3);

//直接量创建
var aList2 = [1,2,3,'asd'];

```

**操作数组中数据的方法**
1、获取数组的长度：aList.length;

```
var aList = [1,2,3,4];
alert(aList.length); // 弹出4

```

2、用下标操作数组的某个数据：aList[0];

```
var aList = [1,2,3,4];
alert(aList[0]); // 弹出1

```

3、push() 和 pop() 从数组最后增加成员或删除成员

```
var aList = [1,2,3,4];
aList.push(5);
alert(aList); //弹出1,2,3,4,5
aList.pop();
alert(aList); // 弹出1,2,3,4

```

4、unshift()和 shift() 从数组前面增加成员或删除成员

```
var aList = [1,2,3,4];
aList.unshift(5);
alert(aList); //弹出5,1,2,3,4
aList.shift();
alert(aList); // 弹出1,2,3,4

```

5、splice() 在数组中增加或删除成员

```
var aList = [1,2,3,4];
aList.splice(2,1,7,8,9); //从第2个元素开始，删除1个元素，然后在此位置增加'7,8,9'三个元素
alert(aList); //弹出 1,2,7,8,9,4

```

**多维数组**
多维数组指的是数组的成员也是数组的数组。

```
var aList = [[1,2,3],['a','b','c']];

alert(aList[0][1]); //弹出2;
```

# js数学对象Math

```
//四舍五入
var res = Math.round(5.921);

//获取最大值
var res = Math.max(10,23,523,43,65,46,32,32);

//获取最小值
var res = Math.min(12312,324,32,42,3,23,412,4332,21,3,-1);

//获取绝对值
var res = Math.abs(-100);

//退一取整
var res = Math.floor(1.9);

//进一取整
var res = Math.ceil(1.1);

//幂运算 用来获取x的y次方 2的3次方
var res = Math.pow(2,3);

//开方运算 返回一个数的平方根
var res = Math.sqrt(9);

random() 返回 0 ~ 1 之间的随机数。
```

## random 返回 0 ~ 1 之间的随机数。

random 获取一个随机数 返回0-1之间的随机小数 有可能到0 ,但是不会取到1

```
//封装函数() 
function rand(m,n){
    return Math.floor(Math.random()*(n-m+1))+m;
}
var res = rand(20,30);
```

