$(document).ready(function(){

        var kuorongP = new Promise(function(resolve, reject){
                        url = "/proprietary/tianyan_api?type=table_name_json&table_name=kuorong_jihua"
                        $.get(url,function(data,status){
                                resolve(data)
                        });
        });

        var chanpinP = new Promise(function(resolve, reject){
                        url = "/proprietary/tianyan_api?type=table_name_json&table_name=kuorong_jihua_chanpin"
                        $.get(url,function(data,status){
                                resolve(data)
                        });
        });
	

html_canvas = `
	<canvas id="paiqi" width = 1000 height = 600 > 
`

width = $('#paiqi').width()
height = '400'
html_canvas = `
	<canvas id="canvas" width = `+width+` height = `+height+`> 
`
	//<canvas id="canvas" width = `+width+` height = `+height+` onmousemove="getXY(event)"> 


kuorongP.then(function(res){
	kuorong = JSON.parse(res)
	console.log(kuorong)

	chanpinP.then(function(res){
		chanpin = JSON.parse(res)
		console.log(chanpin)
		$('#paiqi').append(html_canvas)	

		id="#canvas"
        	var date = new Date();
        	var year = date.getFullYear();
        	var month = date.getMonth()+1;
		var days = new Date(year,month,0).getDate();

		var day_num = date.getDate()
		fangkuai_w = Math.round(width/((days+5)*2))		//---鏃ユ湡瀹藉害
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

		//-------------------------------------------------------------------------------浠婂ぉ璁剧疆棰滆壊鏄剧ず
                	//------绠ご鎵€鎸囨柟鍚戠粯鍒惰摑鑹�
			$('#canvas').setLayer("fangkuai_"+day_num,{
				fillStyle: '#00c1de'  //钃濊壊
    			}).drawLayers();



		start = new Date(year+"-"+month+"-01")
		end = new Date(year+"-"+month+"-"+days)
		krid_list = []  //鏇村叿鎵╁id 璁＄畻鏈€缁堝紑濮� 缁撴潫鏃堕棿
		kr={}
		time_list = []
		n = 0
		id_num = 0 
		//console.log(JSON.stringify(chanpin.slice(0,40)))
			for(i in chanpin.slice(0,50)){  //鍒犻€夊嚭褰撴湀鎺掓湡鎵╁
		
				one_s = new Date(chanpin[i]['鎺掓湡寮€濮嬫椂闂�'])
				one_e = new Date(chanpin[i]['鎺掓湡缁撴潫鏃堕棿'])
		
			    if(one_s > start){

				//鍘婚噸鍒楄〃
				if(krid_list.includes(chanpin[i]['鎵╁ID'])){
					time_list.push(one_s,one_e)
				}
				else{
					//濡傛灉涓嶅瓨鍦ㄨkrid 
					id_num = id_num + 1
					krid_list.push(chanpin[i]['鎵╁ID'])
					n = n+1
				}

					
				s_num = one_s.getDate()
				e_num = one_e.getDate()
				console.log(chanpin[i]['鎺掓湡寮€濮嬫椂闂�'],chanpin[i]['鎺掓湡缁撴潫鏃堕棿'])
				krid = chanpin[i]['鎵╁ID']	
				cpmc = chanpin[i]['浜у搧鍚嶇О']
				xmmc = ''
				ssry = ''
				for(j in kuorong){
					if(kuorong[j]['鎵╁ID'] == krid){
						xmmc = kuorong[j]['椤圭洰鍚嶇О']
						ssry = kuorong[j]['瀹炴柦浜哄憳']
					}
				}
				text2 = xmmc
				text = cpmc
				drawRect()    //----------------------------------------------------------缁樺埗鎺掓湡鐭╁舰

						
				
			    }
			
			//--for end	
			}



	 	//--------鑾峰彇榧犳爣鍧愭爣
	 	//getXY(e)



		//------------------------------------------------------------------------------------------ 绔栫嚎  褰撳墠鏃ユ湡绾�
		i = day_num
		x=x0+(i*2)*fangkuai_w
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
  		  //strokeDash: [5,5],  //铏氱嚎
  		  //strokeDashOffset: 0, //铏氱嚎
                  x1: x, y1: y,
                  x2: x, y2: height,
                });


	 //----绉诲姩渚﹀惉
	 var canvas=document.getElementById("canvas");
	 var bbox=canvas.getBoundingClientRect();
	  day_x_old = day_num
	 canvas.onmousemove = function (e) { 
		var bbox=canvas.getBoundingClientRect();
		x=Math.ceil(e.clientX-bbox.left * (canvas.width / bbox.width));
        	y=Math.ceil(e.clientY-bbox.top * (canvas.height / bbox.height));

	     if(x>x0+fangkuai_w && x<x0+(days)*2*fangkuai_w){
		$('#canvas').setLayer('now_date',{
			x1:x+5,
			x2:x+5,
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


		function drawRect(){	 //缁樺埗 鎺掓湡鏃堕棿
			i = s_num
			x = x0+(i*2)*fangkuai_w
			y = y0+id_num*40
			x_w = (e_num-s_num)*2*fangkuai_w  //闀垮害
			y_w = 30			//瀹藉害
			console.log(krid)
			console.log(x,y)
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



	//---promise end
	});
//---promise end
});



//document end ------------
});
		
