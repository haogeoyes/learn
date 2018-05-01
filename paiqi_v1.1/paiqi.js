$(document).ready(function(){
	
	
var date = new Date();
var year = date.getFullYear();
var month = date.getMonth()+1;

function initPaiQi(year,month){

html_canvas = `
	<canvas id="paiqi" width = 1000 height = 600 > 
`

width = $('#paiqi').width()
height = '400'
html_canvas = `
	<canvas id="canvas" width = `+width+` height = `+height+`> 
`
	//<canvas id="canvas" width = `+width+` height = `+height+` onmousemove="getXY(event)"> 


	console.log(kuorong)

		console.log(chanpin)
		$('#paiqi').empty()
		$('#paiqi').append(html_canvas)	

		id="#canvas"
        	var date = new Date();
        //var year = date.getFullYear();
        	//var month = date.getMonth()+1;
		var days = new Date(year,month,0).getDate();


		
		var day_num = date.getDate()
		//fangkuai_w = Math.round(width*0.9/((days+5)*2))		//---鏃ユ湡瀹藉害
		fangkuai_w = Math.round(width*0.9/((31+5)*2))		//---鏃ユ湡瀹藉害
		x0 = 17+80
		y0 = 17+10
		for(var i=1;i<days+1;i++){	//閬嶅巻鏈湀 澶氬皯澶�
		
			$(id).drawRect({				//------------------------------------------鐢熸垚鏃ユ湡鏂规牸
				name:"fangkuai_"+i,
                	        layer: true,
                       		 //fillStyle: '#00c1de',  //钃濊壊
                       		 fillStyle: ' #001f33',  //榛戣壊 
                        	strokeWidth: 4,
                        	x: x0+(i*2)*fangkuai_w, y: y0,
                        	width: fangkuai_w,
                        	height: fangkuai_w,
				click: function(layer) {
					console.log(layer)
				},
				
                	}).drawText({                 //浜у搧鍚嶅瓧
                        layer: true,
                        draggable: true,        //鏄惁鍏佽鎷栧姩
                        fillStyle: '#ffffff',
                        fontStyle: 'bold',
                        text: i,
                        x: x0+(i*2)*fangkuai_w, y:y0 ,
                        fontFamily: 'Trebuchet MS, sans-serif',
                        fontSize: fangkuai_w/2,
                  })


		//---for end
		}
		
		//---------------------------------------------------------###########---月份
		$(id).drawText({                 
                        layer: true,
                        draggable: true,        
                        fillStyle: '#000',
                        fontStyle: 'bold',
                        text: year+"年"+month+"月",
                        x: x0+((i*2)*fangkuai_w)/2, y:y0-fangkuai_w ,
                        fontFamily: 'Trebuchet MS, sans-serif',
                        fontSize: fangkuai_w/1.5,
                })
		
		
								//---------------------------------###########------下一个月
								i = 32
						    	    date_new = checkMonthJia(year,month)
						    	    year2 = date_new[0]
						    	    month2 = date_new[1]
                $(id).drawText({									
                        layer: true,     
                        fillStyle: '#000',
                        fontStyle: 'bold',
                        text: month2+"月",
                        x: x0+((i*2)*fangkuai_w), y:y0-fangkuai_w ,
                        fontFamily: 'Trebuchet MS, sans-serif',
                        fontSize: fangkuai_w/2,
					 
                  }).drawPolygon({
					  layer: true,
					  fillStyle: '#000',
					  strokeStyle: 'black',
					  strokeWidth: 4,
					  x: x0+((i*2)*fangkuai_w), y: y0,
					  radius: fangkuai_w/1.5,
					  sides: 3,
					  rotate: 90,
					  cursors: {
						    // Show pointer on hover
						    mouseover: 'pointer',
						    // Show 'move' cursor on mousedown
						    mousedown: function(layer) {

						    		initPaiQi(year2,month2)
						    },
						    mouseup: 'pointer'
						  }
					})




								//--------------------------------------------------###########------上一个月		
						    	    date_new = checkMonthJian(year,month)
						    	    year1 = date_new[0]
						    	    month1 = date_new[1]
			$(id).drawText({									
                        layer: true,     
                        fillStyle: '#000',
                        fontStyle: 'bold',
                        text: month1+"月",
                        x: x0-fangkuai_w/20, y:y0-fangkuai_w ,
                        fontFamily: 'Trebuchet MS, sans-serif',
                        fontSize: fangkuai_w/2,
 
                  }).drawPolygon({
					  layer: true,
					  fillStyle: '#000',
					  strokeStyle: 'black',
					  strokeWidth: 4,
					  x: x0-fangkuai_w/20, y: y0,
					  radius: fangkuai_w/1.5,
					  sides: 3,
					  rotate: -90,
					  cursors: {
						    // Show pointer on hover
						    mouseover: 'pointer',
						    // Show 'move' cursor on mousedown
						    mousedown: function(layer) {

						    		initPaiQi(year1,month1)
						    },
						    mouseup: 'pointer'
						  }
					})

	
	
		//-------------------------------------------------------------------------------浠婂ぉ璁剧疆棰滆壊鏄剧ず
                	//------绠ご鎵€鎸囨柟鍚戠粯鍒惰摑鑹�
                	//--------------------------------------------_############----------添加日期判断 ，今日日期如果为本月则激活颜色
          if(year == date.getFullYear() && month == date.getMonth()+1){
          	
          	$('#canvas').setLayer("fangkuai_"+day_num,{
				fillStyle: '#00c1de'  //钃濊壊
    			}).drawLayers();

          }
			

		
		start = new Date(year+"-"+month+"-01")
		end = new Date(year+"-"+month+"-"+days)






		//-----------------#####--------------- 计算扩容产品每个项目有几个产品
		krid_json = {}

    for(i in chanpin.slice(0,500)) {  //鍒犻€夊嚭褰撴湀鎺掓湡鎵╁

        one_s = new Date(chanpin[i]['实施开始时间'])
        one_e = new Date(chanpin[i]['实施结束时间'])

        if(one_s > start && one_e < end) {							//---------#######-------start end

            krid = chanpin[i]['扩容ID']
            if (krid in krid_json) {
                krid_json[krid] = krid_json[krid] + 1
            }
            else {
                krid_json[krid] = 1
            }
        }
     //-----for end
    }

    	console.log(krid_json)




    /*
	//---------------------######-------------绘制产品
    id_num_max = 0
    id_num = 0    //----多少项目
	for(i in krid_json){
        id_num = id_num + 1
			console.log(i,krid_json[i])
			if(krid_json[i]==1){
                createChanPin()
			}
			else{

			}
	}
	id_num_max = id_num
	*/


		
		krid_list = []  //鏇村叿鎵╁id 璁＄畻鏈€缁堝紑濮� 缁撴潫鏃堕棿
		kr={}
		time_list = []
		n = 0
		id_num_max = 0
		id_num = 0 
		//console.log(JSON.stringify(chanpin.slice(0,40)))
			for(i in chanpin.slice(0,500)){  //鍒犻€夊嚭褰撴湀鎺掓湡鎵╁
		
				one_s = new Date(chanpin[i]['实施开始时间'])
				one_e = new Date(chanpin[i]['实施结束时间'])
				console.log(chanpin[i]['实施开始时间'],chanpin[i]['实施结束时间'])
				
		
			    if(one_s > start && one_e < end){							//---------#######-------start end

				//鍘婚噸鍒楄〃
				if(krid_list.includes(chanpin[i]['扩容ID'])){
					time_list.push(one_s,one_e)
                    num_one = num_one + 1
				}
				else{
					//濡傛灉涓嶅瓨鍦ㄨkrid 
					id_num = id_num + 1
					krid_list.push(chanpin[i]['扩容ID'])
					n = n+1
					num_one = 0
				}

					
				s_num = one_s.getDate()
				e_num = one_e.getDate()
				//console.log(chanpin[i]['鎺掓湡寮€濮嬫椂闂�'],chanpin[i]['鎺掓湡缁撴潫鏃堕棿'])
				krid = chanpin[i]['扩容ID']	
				cpmc = chanpin[i]['产品名称']
				xmmc = ''
				ssry = ''
				for(j in kuorong){
					if(kuorong[j]['扩容ID'] == krid){
						xmmc = kuorong[j]['项目名称']
						ssry = kuorong[j]['实施人员']
					}
				}
				text2 = xmmc
				text = cpmc
				if(krid_json[krid] == 1){

                    createChanPin()    //----------------------------------------------------------缁樺埗鎺掓湡鐭╁舰
				}
				else{
                    num = krid_json[krid]
					//for( k = 0;k<num;k++){
                        createChanPinList(num,num_one)
						y_w = 30
                    	y = y0 + id_num * 40
                    	$(id).drawText({                 				//-----------------宸﹀垪 澶� 椤圭洰鍚嶇О
                            layer: true,
                            draggable: true,        //鏄惁鍏佽鎷栧姩
                            fillStyle: '#000000',
                            fontStyle: 'bold',
                            text: text2,
                            //text: xmmc,
                            x: x0 - 80, y: y + (y_w / 4),
                            fontFamily: 'Trebuchet MS, sans-serif',
                            fontSize: y_w / 2,
                            fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
                        })

					//}
				}

						
				
			    }
			
			//--for end	
			}
			id_num_max = id_num
			console.log(id_num,krid_list)




	 	//--------鑾峰彇榧犳爣鍧愭爣
	 	//getXY(e)



		//------------------------------------------------------------------------------------------ 绔栫嚎  褰撳墠鏃ユ湡绾�

                	//--------------------------------------------_############----------添加日期判断 ，今日日期如果为本月则激活颜色
          if(year == date.getFullYear() && month == date.getMonth()+1){
          		i = day_num
				x=x0+(i*2)*fangkuai_w
          }	
          else{
          	    x = 1000000
          }


		y = y0+18
                $('#canvas').drawLine({
               	  layer: true,
		  name:'now_date',
                  strokeStyle: '#00a65a', //缁胯壊
                  strokeWidth: 4,
                  rounded: true,
                  startArrow: true,
                  arrowRadius: 15,
                  arrowAngle: 60,
                  opacity: 0.7,
  		  //strokeDash: [5,5],  //铏氱嚎
  		  //strokeDashOffset: 0, //铏氱嚎
                  x1: x, y1: y,
                  x2: x, y2: height,
                }).drawRect({	//-------------------------################-----------添加x轴 矩形框选择
                	  name:'now_xiangmu',
				  layer: true,
				  strokeStyle: '#00a65a',
				  fromCenter: false,
				  strokeWidth: 3,
				  x: x0-90, y: 100000,
				  width: x0+(days)*2*fangkuai_w+20,
				  height: y_w+10,
				  cornerRadius: 10,
				  //strokeDash: [5],
				  opacity: 0.1,
				  fillStyle: '#00a65a',
				});
                
         
                


	 //----绉诲姩渚﹀惉
	 var canvas=document.getElementById("canvas");
	 var bbox=canvas.getBoundingClientRect();
	  day_x_old = day_num
	 canvas.onmousemove = function (e) { 
		var bbox=canvas.getBoundingClientRect();
		x=Math.ceil(e.clientX-bbox.left * (canvas.width / bbox.width));
        	y=Math.ceil(e.clientY-bbox.top * (canvas.height / bbox.height));


		//---添加 横轴坐标提示
		num = parseInt((y-y0)/40)
		id_num = num
		y_xiangmu = y0+id_num*40
		//console.log(x,y,num,y_xiangmu)


	     if(x>x0+fangkuai_w && x<x0+(days)*2*fangkuai_w && id_num > 0 && id_num <= id_num_max){          //---###########-----添加y轴方向 取值范围
		$('#canvas').setLayer('now_date',{
			x1:x+5,
			x2:x+5,
 		 }).setLayer('now_xiangmu',{       //------##############---鼠标移动改变y值
			y:y_xiangmu-5,
			
    		})
		
		
		day_x1 = (x+5-x0)/(2*fangkuai_w)
		day_x = Math.round((x+5-x0)/(2*fangkuai_w))
		//console.log(x,y,day_x,day_x1,day_x_old)


		//------鍏ㄩ儴缁樺埗榛戣壊
		for(var i=1;i<days+1;i++){	//閬嶅巻鏈湀 澶氬皯澶�
			$('#canvas').setLayer("fangkuai_"+i,{
				fillStyle: ' #001f33'
    			})
		}
		//------绠ご鎵€鎸囨柟鍚戠粯鍒惰摑鑹�
			$('#canvas').setLayer("fangkuai_"+day_x,{
				fillStyle: '#00c1de'  //钃濊壊
    			}).drawLayers();
			day_x_old = day_x
	    //--if end
	    }
	//--move end
	}	



	//----------------fun----------------


		function createChanPin(){	 //缁樺埗 鎺掓湡鏃堕棿
			i = s_num
			x = x0+(i*2)*fangkuai_w
			y = y0+id_num*40
			x_w = (e_num-s_num)*2*fangkuai_w  //闀垮害
			y_w = 30		//瀹藉害
			console.log(krid)
			console.log(x,y)
			console.log(e_num,s_num)
			console.log(x_w,y_w)
			console.log(s_num,e_num)
			$(id).drawRect({				//---鐢熸垚鏃ユ湡鏂规牸
                	        layer: true,
                       		fillStyle: '#00c1de',  //钃濊壊
                        	draggable: true,        //鏄惁鍏佽鎷栧姩
                        	strokeWidth: 4,
                        	x: x, y: y,
                        	width: x_w,
                        	height: y_w,
                        	opacity: 0.5,
				cornerRadius: 10,
				fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
				click: function(layer) {
					console.log(layer)
				},
				
                	}).drawText({                 //
                        layer: true,
                        draggable: true,        //鏄惁鍏佽鎷栧姩
                        fillStyle: '#000000',
                        fontStyle: 'bold',
                        text: text,
                        //text: xmmc,
                        x: x+(y_w/2), y:y+(y_w/4),
                        fontFamily: 'Trebuchet MS, sans-serif',
                        fontSize: y_w/2,
			fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
                      }).drawText({                 				//-----------------宸﹀垪 澶� 椤圭洰鍚嶇О
                        layer: true,
                        draggable: true,        //鏄惁鍏佽鎷栧姩
                        fillStyle: '#000000',
                        fontStyle: 'bold',
                        text: text2,
                        //text: xmmc,
                        x: x0-80, y:y+(y_w/4),
                        fontFamily: 'Trebuchet MS, sans-serif',
                        fontSize: y_w/2,
			fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
                      })



		//--fun end
		}


    function createChanPinList(num,num_one) {	 //缁樺埗 鎺掓湡鏃堕棿
        i = s_num
        x_w = (e_num - s_num) * 2 * fangkuai_w  //闀垮害
        y_w = 30/(num)		//瀹藉害
        x = x0 + (i * 2) * fangkuai_w
        y = y0 + id_num * 40 + y_w*num_one
        console.log(krid)
        console.log(x, y)
        console.log(e_num, s_num)
        console.log(x_w, y_w)
        console.log(s_num, e_num)
        $(id).drawRect({				//---鐢熸垚鏃ユ湡鏂规牸
            layer: true,
            fillStyle: '#00c1de',  //钃濊壊
            draggable: true,        //鏄惁鍏佽鎷栧姩
            strokeWidth: 4,
            x: x, y: y,
            width: x_w,
            height: y_w,
            opacity: 0.5,
            cornerRadius: 10,
            fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
            click: function (layer) {
                console.log(layer)
            },

        }).drawText({                 //
            layer: true,
            draggable: true,        //鏄惁鍏佽鎷栧姩
            fillStyle: '#000000',
            fontStyle: 'bold',
            text: text,
            //text: xmmc,
            x: x + (y_w / 2), y: y + (y_w / 4),
            fontFamily: 'Trebuchet MS, sans-serif',
            fontSize: y_w / 2,
            fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
        })/*.drawText({                 				//-----------------宸﹀垪 澶� 椤圭洰鍚嶇О
            layer: true,
            draggable: true,        //鏄惁鍏佽鎷栧姩
            fillStyle: '#000000',
            fontStyle: 'bold',
            text: text2,
            //text: xmmc,
            x: x0 - 80, y: y + (y_w / 4),
            fontFamily: 'Trebuchet MS, sans-serif',
            fontSize: y_w / 2,
            fromCenter: false,    //浠ョ煩褰㈤《鐐瑰潗鏍囩粯鍒�
        })*/


    //--fun end
	}








        return month
//-----fun end  initPaiqi end
}

var month = initPaiQi(year,month)



function checkMonthJia(year,month){    //month 加一个月
	if( month == 12){
		month = 1
		year = year + 1
	}
	else{
		month = month + 1
	}
	return [year,month]
}
function checkMonthJian(year,month){    //month 减一个月
	if( month == 1){
		month = 12
		year = year - 1
	}
	else{
		month = month - 1
	}
	return [year,month]
}


//document end ------------
});
		
