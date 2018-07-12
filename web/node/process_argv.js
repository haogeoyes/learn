console.log(process.argv)
let num1 = process.argv[2] - 0
let num2 = process.argv[3] - 0 //parseInt
let num = num1 + num2
setTimeout(()=>{
	console.log(num)
},2000)

