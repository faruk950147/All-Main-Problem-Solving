arr = [1, 2, 3, 4, 5];
sum = 0;
// arr.forEach(function(value,index,array) {
//     console.log("Value: " + value + " Index: " + index + " Array: " + array);
// });

// arr.forEach(function(value) {
//     sum += value;
// });
// console.log(sum);

function forEach(arr,callback) {
    for (let i = 0; i < arr.length; i++) {
        callback(arr[i], i, arr);
    }
}