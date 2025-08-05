// pure function
function add(x, y) {
    return x + y;
}
// console.log(add(2, 3));

// first class function
// const add = function(x, y) {
//     return x + y;
// }
// console.log(add(2, 3));

// higher order function
function mainFunction(a, b, func) {
    let c = a + b;
    let d = a - b;
    function multiply( ) { 
        console.log(c, d);
        let x = func(c, d);
        console.log(x);
        return c * d * x;
    }
    return multiply();
}
console.log(mainFunction(2, 3, add));
