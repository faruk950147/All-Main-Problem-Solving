function add(a, b) {
    return a + b;
}
function currying(fn) {
    return function (a) {
        return function (b) {
            return fn(a, b);
        };
    };
}
console.log(currying(add)(1)(2));