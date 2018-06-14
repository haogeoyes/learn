define(["jquery","service/salemanService","saleman/add","saleman/edit"],function($,salemanService,salemanAdd,salemanEdit){
    return function(){

        console.log("数据服务：",salemanService)
        
        //渲染出一个销售员列表页面
        //a、拼接出一整个DOM字符串
        var str=`<div>
                    <div>操作：
                        <button class="add" >添加</button>
                        <button>查询</button>
                    </div>
                    <table border="10" cellpadding="30">
                        <thead>
                            <tr>
                                <th>姓名</th>
                                <th>年龄</th>
                                <th>操作</th>
                            </tr>
                        </thead>
                        <tbody>
                        ${salemanService.getList().map(item=>{
                            return `<tr><td>${item.name}</td><td>${item.age}</td><td>
                            <button data-tr="${item}" class="str_edit">编辑</button></td></tr>`
                        }).join("")}
                        </tbody>
                    </table>
                </div>`;
        //b、把字符串插入到指定的区域中
        var $saleman=$(str);

        //进行添加操作
        $saleman.on("click",".add",function(){
        // $saleman.on("click",function(){
        //     console.log(this.hasClass('add'))
        //     if($(this).hasClass("add")){
        //         console.log(22222)
        //     }
            salemanAdd();
        })
        $saleman.on("click",".str_edit",function(){
            console.log(this)
        })
        // $saleman.on("click","button",function(){
        //     // console.log(this.hasClass(''))
        //     console.log(this)
        //     console.log(222222)
        //     // salemanEdit();
        // })

        $("#main .content").html($saleman);

    }
})