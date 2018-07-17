const express = require('express')
let app = express();
app.listen(8888,()=>{
    //启动完成
})
app.use('/url',(req,res,next)=>{  //按代码顺序执行
    console.log('111111')
    next()  //继续   当没 写返回
}) //一件事
app.use('/url2',(req,res,next)=>{  //按代码顺序执行
    console.log('url2')
    next()  //继续   当没 写返回
}) //一件事
	
