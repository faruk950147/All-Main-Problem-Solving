function simple(a, b, callback) {
    return callback(a, b);
}
function add(a, b) {
    return a + b;
}
function sub(a, b) {
    return a - b;
}
function mul(a, b) {
    return a * b;
}
function div(a, b) {
    return a / b;
}
console.log(simple(10, 20, add));
console.log(simple(10, 20, sub));
console.log(simple(10, 20, mul));
console.log(simple(10, 20, div));