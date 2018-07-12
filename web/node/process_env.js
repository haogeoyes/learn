//console.log(process.env)

//let 块级变量
let stuOrTeacher = process.env.MY_TEST;
if(stuOrTeacher === 'me'){
	console.log('me')
}else{
	console.log('no')
}

