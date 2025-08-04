function add(a, b) {
    return a + b;
}
console.log(add(2, 3));

function sub(a, b) {
    return a - b;
}
console.log(sub(2, 3));

function mul(a, b) {
    return a * b;
}
console.log(mul(2, 3));

function div(a, b) {
    return a / b;
}
console.log(div(2, 3));

function mod(a, b) {
    return a % b;
}
console.log(mod(2, 3));

function pow(a, b) {
    return a ** b;
}
console.log(pow(2, 3));

function fact(a) {
    let fact = 1;
    for (let i = 1; i <= a; i++) {
        fact *= i;
    }
    return fact;
}
console.log(fact(5));
