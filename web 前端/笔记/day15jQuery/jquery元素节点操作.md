## jquery元素节点操作

**创建节点**

```
var Div = $('<div>');
var Div2 = $('<div>这是一个div元素</div>');
```

**插入节点**
1、append()和appendTo()：在现存元素的内部，从后面插入元素

```
var Span = $('<span>这是一个span元素</span>');
$('#Div1').append(Span);
......
<div id="div1"></div>
```

2、prepend()和prependTo()：在现存元素的内部，从前面插入元素

3、after()和insertAfter()：在现存元素的外部，从后面插入元素

4、before()和insertBefore()：在现存元素的外部，从前面插入元素

**删除节点**

```
$(element).remove() 删除当前元素
$(element).empty()清空
```

**克隆节点**

```
$(element).clone(true)
```