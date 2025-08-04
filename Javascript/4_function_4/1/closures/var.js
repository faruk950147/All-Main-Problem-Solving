// var is function scope 
// allow redeclaration
// allow hoisting

var num = 10;
function add() {
    var num2 = 20;
    function add2() {
        var num3 = 30;
        console.log(num + num2 + num3);
    }
    add2();
}
add();

var num = 10;
num = 20;
function add() {
    var num2 = 20;
    function add2() {
        var num3 = 30;
        console.log(num + num2 + num3);
    }
    add2();
}
add();
