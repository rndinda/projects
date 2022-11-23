
//1.Grab the needed values
function calc() {
var a = parseInt(document.querySelector('#val_1').value);
var b = parseInt(document.querySelector('#val_2').value);
var c = document.querySelector('#val_3').value;
var calculate;

//2.calculate the values
if (c == 'add'){
    calculate = a + b;
}else if(c == 'min'){
    calculate = a - b;
}else if (c == 'div'){
    calculate = a / b;
}else if(c == 'mult') {
    calculate = a * b;
}
//3.output in website
document.querySelector('#result').innerHTML = calculate;
}