// let and const are block scope
// let and const are not allowed to redeclare
// let and const are allowed to reassign    
// let and const are not allowed to hoist
// let and const are constant

// var is function scope
// var is allowed to redeclare
// var is allowed to reassign
// var is allowed to hoist
// var is not constant
// example let and const
// let a = 10;
// //  it is not allowed to redeclare
// let a = 20;
// console.log(a);

// it is allowed to reassign
// let a = 10;
// a = 20;
// console.log(a);

// it is not allowed to hoist
// console.log(b);
// let b = 10;

// example const
// const c = 10;
// it is not allowed to redeclare
// const c = 20;
// console.log(c);

// it is not allowed to reassign
// const c = 10;
// c = 20;
// console.log(c);

// it is constant
const d = 10;
console.log(d);

// block scope
if (true) {
    let e = 10;
    console.log(e);
}
console.log(e);


// function scope
function f() {
    let f = 10;
    console.log(f);
}
f();
console.log(f);

// const scope
function g() {
    const g = 10;
    console.log(g);
}
g();
console.log(g);

