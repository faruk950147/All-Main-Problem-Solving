var a = 5;

function display() {
    // it is not allowed to redeclare in global scope var a = 10;
    // it is allowed to only reassign
    a += 10;
    var b = 10;
    console.log("Inside a: " + a);
    // it is allowed to declare in function scope var b = 10;
    console.log("Inside b: " + b);
}
display();
console.log("Outside a: " + a);