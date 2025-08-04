// function memorization(fn) {
//     const cache = {};
//     return function (n) {
//         if (cache[n]) {
//             return cache[n];
//         }
//         const result = fn(n);
//         cache[n] = result;
//         return result;
//     };
// }

function add(a, b) {
    return a + b;
}

const memorizedAdd = memorization(add);
console.log(memorizedAdd(1, 2));