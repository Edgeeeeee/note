# 相关尺寸

**获取元素相对于文档的偏移量**

> var pos = $('#small').offset(); 
>
> // console.log(pos.left);// console.log(pos.top);

**获取当前元素相对于父级元素的偏移量**

> var l = $('#small').position().left;
>
> var t = $('#small').position().top;
>
> // console.log(l,t);

**获取文档滚动距离**

> var st = $(document).scrollTop();
>
> var sl = $(document).scrollLeft();

**获取元素的宽度和高度**

> var w = $('#big').width();
>
> var h = $('#big').height();

**设置元素的宽度和高度**

> $('#big').width(400);
>
> $('#big').height(400);
>
> // console.log(w,h);

**获取可视区域的宽度和高度**

> var cw = $(window).width();
>
> var ch = $(window).height();

**获取文档的宽度和高度**

> var cw = $(document).width();
>
> var ch = $(document).height();
>
> console.log(cw,ch);



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

