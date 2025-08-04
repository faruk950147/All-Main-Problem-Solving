
let num1 = 80
let num2 = 20
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
let add3 = function () {
    let num3 = 50;
    return function () {
        return num1 + num3;
    }
}
// this is most common use of closure
let sum3 = add3();
console.dir(sum3);
console.log(sum3());