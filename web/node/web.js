const http = require('http')
let server = http.createServer()
server.on('request',(req,res)=>{
    res.end('xxxxxx')
})
server.listen(8888,()=>{
    console.log('服务器启动888端口')
})
