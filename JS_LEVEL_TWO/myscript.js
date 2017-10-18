function hello() {
  console.log("Hello World!");
}

function addNum(num1,num2) {
  console.log(num1+num2);
}

function helloSomeone(name="Mahmud") {
  console.log("Hello "+name);
}

function formal(name="Sam", title="Sir") {
  console.log(title+ " " +name );
  return title+ " " +name;
}

function timesFive(numInput) {
  var result=numInput*5;
  return result
}

// Global scope
var v=" Global V"
var stuff=" Global Stuff"

function fun(stuff) {
  console.log(v);
  stuff="Reassign stuff inside func"
  console.log(stuff);
}

fun();
console.log(stuff);
