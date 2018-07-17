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
server.use(router)
server.listen(8888)
