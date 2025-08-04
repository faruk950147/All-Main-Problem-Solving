
let arr = [1,2,3,4,5];
// let sum = arr.reduce(function (prev, curr, index, array) {
//     console.log(prev, curr, index, array);
//     return prev + curr;
// }, 0);
// console.log(sum);

function reduce(arr, callback, initial) {
    let result = initial;
    for (let i = 0; i < arr.length; i++) {
        result = callback(result, arr[i], i, arr);
    }
    return result;
}
console.log(reduce(arr, function (prev, curr, index, array) {
    console.log(prev, curr, index, array);
    return prev + curr;
}, 0));