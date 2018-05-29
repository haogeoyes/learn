#获取元素
- 获取一个
- 获取全部元素
- 操作类样式 添加 移除 切换

#data- 自定义属性
懒加载 使用？？？
自定义属性  和 绑定id 对应
3点 如何获取 如何设置 

#文件读取 api
- input file
  - one change 事件
     input.onchange=function(){
		for(){
		}
	}
     读取文件加载文件 onload 异步事件

#获取网络状态
- window.navigator.ononline
- ononline
- onoffline 事件 触发条件

#获取地理定位
- window.navigator.geolocation 经纬度 只能获取一次
- 实时获取位置消息

#本地存储
- local  永久 20M  页面共享
- session 当前浏览器有效 
- window.localstorage.setitem get remove clean

#操作多媒体  作业
- Dom 参考
- 完成一个在线播放器 网页云音乐 播放 下载 快进 跳播功能时间对应

#canvas
- 统计图 
- 小游戏  数据处理 图像处理
- 1.落笔坐标点 2.连线 3.描边 stroke()
- stroke()  多个 会重绘 描边 
- fill 填充 
- 非零环绕原则 正时针绘制 逆时针绘制 方向相反 射线 相交越少越好
  - 闭合 而且方向相反 点 射线 相交 +1 -1 为0 进行填充 顺逆时针
- biginpath（） 开启新图层  ctx.beginPath
- linewidth 线宽
- 虚线 ctx.setLineDash（【实线，空白，实线，空白】）
- 绘制动画 
  - rect 矩形
  - content.clearRect 清除

--作业：
	1. 从200,100的位置绘制宽为200高为150的矩形
        2. 准备一个600*400的画布，三等分这个画布，分别绘制正方形。直角三角形，梯形
- 线性渐变
- 绘制文本 填充文本 描边文本
- 绘制图片 content.drawImage   添加onload 事件后再开始绘制
	- 截图 绘制到哪
	- 不失真 宽高比
- 弧度 content.arc  绘制o度角 3点 角度为起点 往下6点90度为整网上为负 
	- 弧度制  math.pi*3 度  cos math.cos()*100
- 平移 ctx.translate
- 旋转 

#typora
#markdown
	- https://www.zybuluo.com/mdeditor




# 20180529 js 构造函数
function fn(name){
	this.name = name
}
var _n = new fn('小明');

## 构造函数方式2  重点jQuery 核心 原型
属性查找规则
1、变量声明了未赋值才是undefined 2、属性不存在也是undefined

上下文调用方式   最强大
call apply bind
function f1(){
	console.log(this)
}

只有对象才有原型
//第一个参数决定 this的值
f1.call([1,2,3])

bind 延迟执行  call apply 执行过程中绑定了 this值
动画 canvas 延迟函数 
setTimeout(function(){
	console.log(this)	
},50)
call、apply是立刻执行了这个函数，并且执行过程中绑定了this的值
bind并没有立刻执行这个函数，而是创建了一个新函数，新函数绑定了this的值
课外作业 5.29  思考bind 如何实现  如何解决浏览器的兼容问题



# es6
> 模板字符串
- var s1 = `111`
- 解决痛点  字符串拼接
- var s1 = `hello ${name}`
```
	var a = `<div>
			<span></span>
		 </div>`
```
- app 开发 react native？weex？
> 解构赋值
```
	获取对象
	var obj = {name:'aa',age:18}
	let { name,age } = obj;  //obj.name 创建了两个变量
```
- 减少全局变量污染?
- 有什么作用  可以节省一二写字符
```
	//使用结构赋值
	function fn(option){
		//option.width
	}
	fn({
		width:100,
		height:100,
		age:50
	})

	//接受对象自变量  局部变量
	function fn_2({ width,height,age}){
		console.log(width,height,age)
	}

```
- 其他用法
```
	var { name:obj2Name } = obj  //创建新变量 obj2Name
```
- 属性的简写
```
        var a = 3 ; var b = {a} ; console.log(b); // {a:3}
	var c = 4
	var d = {a,c}
        {a} === {a: a}
```

> rest 参数
```
	function fn(){
		//arguments 函数内部局部变量  调用函数传递的是实参数
		console.log(arguments.length)
		//第一个实参
		console.log(arguments[0])
		for(i in arguments){
			console.log(arguments[i])
		}
	}
	fn(1,2,3,4,5)
```
- es6 箭头函数内部不能使用arguments
		- rest 参数弥补这个问题
```
	// ...args rest参数的使用方式
	//产生了一个变量，是数组，包含所有实参
	function fn(...args){
		//验证数组
		console.log(args instanceof Array)
		console.log(Object.prototype.toString.call(args))  //"[object Array]"
		console.log(Array.isArray(args)) //es5 方法
		console.log(args)
	}
	fn(1,2,3)
```
+ typeof
	- typeof 智能判断 数字 字符 布尔 undefined 函数
+ Object.prototype.toString.call()
	- 5 '[object NUmber]'
	- [object String]
	- [object Boolean]
	- [object Null]
	- [object Undefined]
	- [object Array]
	- [object Function]
	- [object Date]
	- [object RegExp]





