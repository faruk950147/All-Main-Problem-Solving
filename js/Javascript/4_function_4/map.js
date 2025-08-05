let arr = [1,2,3,4,5];
// let sqrt = arr.map(function(value){
//     // return Math.random() * 10;
//     return value * value;
// })
// console.log(sqrt);

function map(arr, callback) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(callback(arr[i], i, arr));
    }
    return result;
}
sqrt = map(arr, function(value, index, array){
    return value * value;
})
console.log(sqrt)