# 关于事件

## 事件绑定

1.**基本绑定**

> $(element).click(function(){})
>
> $(element).dblclick(function(){})
>
> 。。。
>
> 加载完毕事件
>
> $(document).ready(function(){})
>
> $(function(){})

2.**方法绑定**

> $(element).bind('click', function(){})//绑定事件
>
> $(element).unbind();//解除事件绑定

3.**动态绑定**

> $(element).live('click', function(){})
>
> 需注意，live方法在高版本的jquery中移出了,在使用时请注意版本

## 事件触发

> 当我们想要去触发某个元素的事件时可以使用 trigger,注意需指定元素的事件类型

```
$(element).trigger('click')
```

### 常用的鼠标事件

```
鼠标单击事件 click
鼠标双击事件 dbclick
鼠标移入事件 mouseover
鼠标移出事件 mouseout
鼠标按下事件 mousedown
鼠标抬起事件 mouseup
鼠标移动事件 mousemove
```







## 事件冒泡和默认行为

**事件冒泡**

> 当触发一个元素的事件时,会**自动触发该元素的父级和先辈级的同类型事件**,**造成事件并发**,导致页面混乱,我们称为事件冒泡
>
> 此时我们可以在元素的事件处理函数中 返回一个false 来进行阻止,注意这个方法仅限于在jquery中使用

**默认行为**

> 在页面中有些元素是具备默认行为的,例如a链接的单击,表单的提交,都会进行跳转或提交,这些我们成为默认行为
>
> 但是在绑定上事件后,**它首先会先执行事件,再去执行默认行为**,而有时我们只想让其触发事件,但不执行默认行为时,
>
> **我们可以在该元素的事件中 返回一个false来进行阻止默认行为**

```
<a href="http://www.baidu.com">百度</a>


$('a').click(function(){

    //阻止默认行为
    return false;
})
```

**获得当前鼠标的位置和按键**

> 我们有鼠标和键盘按键的事件,在触发事件时如果我们**想要获取鼠标的位置或键盘按键信息时**,
>
> 首先需要在当前的事件中**传递一个 事件对象 e**vent

```
$(element).click(function(e){
    //能够获取鼠标的x轴和y轴坐标,坐标位置相对于浏览器窗口
    var x = e.clientX;
    var y = e.clientY;

    //能够获取鼠标的x轴和y轴坐标,坐标位置相对于文档
    var _x = e.pageX;
    var _y = e.pageY;
})

$(element).keydown(function(e){
    //可以打印e对象,或者直接使用该对象中的keyCode属性来获取按键信息
    var key = e.keyCode;
    console.log(key);
})
```