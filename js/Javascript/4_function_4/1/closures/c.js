// normal function
// function add(a, b) {
//     return a + b;
// }
// console.log(add(2, 3));
// Scope global

// let num1 = 80
// let num2 = 20
// not a closure but advantage of closure
// let add = function () {
//     return num1 + num2;
// }
// this is most common use of closure
// let sum = add();
// console.dir(sum);
// console.log(sum());


// // not a closure because num1 is not in the scope of add2 but advantage of closure
// let add2 = function () {
//     let num3 = 50;
//     return num1 + num3;
// }
// this is most common use of closure
// let sum2 = add2();
// console.dir(sum2);
// console.log(sum2());

//it is a closure because num1 and num2 are in the scope of add3
// let add3 = function () {
//     let num3 = 50;
//     return function () {
//         return num1 + num3;
//     }
// }
// // this is most common use of closure
// let sum3 = add3();
// console.dir(sum3);
// console.log(sum3());


// var num3 = 50;
// var num4 = 10;
// var add4 = function () {
//     var num5 = 20;
//     return function () {
//         return num3 + num4 + num5;
//     }
// }
// var sum4 = add4();
// console.dir(sum4);  

(function () {
    var num6 = 30;
    var add6 = function () {
        var num7 = 40;
        if (num6 < num7) {
            console.log(num6);
        }
    }
    console.dir(add6);
})();