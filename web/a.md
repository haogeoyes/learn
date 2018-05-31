## 获取元素
- 获取一个
- 获取全部元素
- 操作类样式 添加 移除 切换

## data- 自定义属性
懒加载 使用？？？
自定义属性  和 绑定id 对应
3点 如何获取 如何设置 

## 文件读取 api
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

## 本地存储
- local  永久 20M  页面共享
- session 当前浏览器有效 
- window.localstorage.setitem get remove clean

## 操作多媒体  作业
- Dom 参考
- 完成一个在线播放器 网页云音乐 播放 下载 快进 跳播功能时间对应

## canvas
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

## typora
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
> 箭头函数
- 箭头函数就是为了绑定匿名函数
```
	//无参匿名函数
	div.onclick=function(){}
	div.onclick=()=>{}
	//有参数
	var fn=name=>{console.log(name)}
	var fn=(name)=>{}
```
> 匿名函数
```
	var status = [1,2,3]
	status.forEach(function(value,index){
	})
	status.forEach(value=>{
	})
```
+ 阮一峰
+ 箭头函数和匿名函数有哪些不同？  重点
	- 函数 作用域
	- 箭头函数不能作为构造函数
	- 不可以使用arguments对象
	- 不可以使用yield命令
	- Generator函数经常用async替代
```
	var p={
		age:18,
		run:()=>{
			setTimeout(()=>{
			 //默认指向this windows方法
				console.log(this)
			},1000)
			//外层函数 作用于是全局作用域
		}
		say:function(){
			setTimeout(()=>{
			 	//默认指向p对象 
				console.log(this)
			},1000)
		}
		//es6为了解决这种问题

		//es6对象方法简写  推荐使用的匿名函数书写方式
		say(){
			console.lg(this)
		}
	}
```

+ 实际中用ES6的话,兼容性上是不是不太好? 用bable插件

> bable 插件 https://www.babeljs.cn
+ vue 脚手架 vue-cli内置了babel，如果需要可以修改兼容版本

## vscode 好看简洁 强大 sublime webstorm
+ https://marketplace.visualstudio.com/items?itemName=ruakr.ftp-kr
+ https://www.javascriptcn.com/read-7177.html

## mnd 开发社区
+ https://developer.mozilla.org/zh-CN/



# 20180531 JS高级
## bind方法实现
+ 1、bind方法放在函数的原型中
```
	Function.prototype._bind = function(target){
		return function(){}  //不可以
		//利用闭包 创建内部函数  返回新函数
		return (function(){
			//执行fn里面的逻辑
			this.call(target);
		})()
	}
	function fn(
		console.log(this)
	){}
	fn.bind({age:18})
	var _f3 = fn.bind({age:11})
	_f3()
```

##对象的扩展
```
	Object.assign 对象的浅拷贝
	var source={age:18,height:170}
	//克隆新对象
	var target={};
	var newObj = Oject.assign({},source)
```


##回调地狱 Permise
```
	function f1(){
		setTimeout(()=>{
			console.log(1)
		},1000)
	}
	function f2(){ return new Permise(resolve=>{
		//告诉外界我已经执行完了
		resolve()
		})
	}
	f1().then(res=>{
		return f2();
	}).then(res=>{
		return f3();
	})
```
+ promise es6  sync es8
+ rxjs
+ Promise 错误处理方式
```
	function getPromise(fn){
		return new Promise(resove=>{
			$.get('/apie',function(res){
				//res
			})

		})
	}
	getPromise().then(res=>{
		//res 服务器中获取数据
	})

	function getPromise(fn){
		return new Promise(resove=>{
			$.ajax({
				url:'/api',
				success(res){
					resolve(res);  //成功
				},
				error(res){
					reject(resError); //失败处理
				}
			})

		})
	}

	getPromise().then(res=>{
	
	},resError=>{
		console.log(resError)
	})
	//第一个参数成功回调   第二个参数 失败回调


	第二种错误处理方式
	getPromise.then(res=>{
		//成功
	}).catch(resError=>{
		//失败
	})

	//区别 ，推荐第二种
	//第二种 强大  不仅仅可以捕获到 reject 传递的参数
	//还可以捕获到 成功的毁掉中发生的错误

```
+ catch
```
	function f1(name){
		return new Promise((resolve,reject)=>{
			setTimeout(()=>{
				if(name=='a'){
					resolve('成功')
				}else{
					reject('失败')
				}
			})
		})
	}
	f1('a').then(res=>{console.log(11111)})
	f1('a').then(res=>{
		console.log(11111)
		var a=5;
		a();  //代码发生了错误
	}).catch(res=>{
		console.log(res);
		//成功中失败的代码也能捕获
		
	})
```
## async
```
	(async function(){
		//异步操作 函数f1()
		await f1();
		console.log('第一步')
		await f1();
		console.log('第二步')
	})()


	function q(){
	    return new Promise((resolve)=>{
		setTimout(()=>{
			resolve("hi")	;
		},1000)
	    })
	}
	(async function(){
		const res = await q();
		let res = await q();
		const res1 = await q();
	})()


	var p = {
		say:async ()=>{
			await q();
		},
		run:async function(){
			await q();
		}
	}

    try{
	(async ()=>{
		let res = await p.say();
		console.log(res)
		await p.run();
	})()
    }catch(e){	
	console.log(e)
    }

```
+ async 处理返回值
	- let 
	- const
```
	async function get(){
		var let res = await  timer()
	}
	get()
```
+axios 也可以异步操作


## class 类语法  原型继承的根
```
	function a(name,age){
		this.name = name;
		this.age = age;
	}
	one = new a('hao',12)
	//类的样式
	class p{
		//构造方法
		constructor(name,age){
			this.name = name
			this.age = age
		}
	}
	var s = new p('hao',18)
```
+ class 类的方法
```
	function p(){
	}
	p.prototype.run=()=>{
		console.log('run')
	}
	class s{
		constructor(age){
			this.age = age
		}
		run(){
			console.log(`run class ${this.age}`)  //模板字符串
		}
		static down(){
			console.log('class 类的静态方法')
		}
	}
	var s1 = new s(18);
```
+ 类的静态方法 static down(){}
	- p.down()
+ 类的静态属性  通过自身属性访问的this static down(){}
	- p.age
+ 类的继承  (原型继承）
```
		class p{
			constructor(name){
				this.name = name
			}
		}
		class a extends p{
			constructor(){
				super(name);  //调用父类构造方法
				//通过super 继承了name属性
				this.age = age //自身构造属性
			}
		}
```

## model 模块
## 框架封装


