const express = require('express')
let server = express();
let router = express.Router();

router.get('/login',(req,res)=>{  //按代码顺序执行
    console.log('url1')
    res.end('login')//页面返回
}) //一件事
.get('/logout',(req,res)=>{
    res.end('logout')
})
.get('/json',(req,res)=>{
    res.json([{name:'aaa'}])
})
.get('/redirect',(req,res)=>{
    res.redirect('http://www.baidu.com')
})
.get('/jsonp',(req,res)=>{
    res.jsonp('jsonp')
})
.get('/download',(req,res)=>{
    res.download('http://www.baidu.com')
})



server.use(router)
server.listen(8888)
