let arr = [1,2,3,4,5];
// let sqrt = arr.filter(function(value){
//     return value % 2 == 0;
// })
// console.log(sqrt);

// let arr1 = arr.filter(function(value){
//     return value % 2 === 0;
// })
// console.log(arr1)

function filter(arr, callback) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (callback(arr[i], i, arr)) {
            result.push(arr[i]);
        }
    }
    return result;
}
console.log(filter(arr, function(value){
    return value % 2 === 0;
}))
