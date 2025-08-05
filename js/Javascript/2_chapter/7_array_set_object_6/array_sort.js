let arr = [5, 1, 0, 2, 4, 3];
// arr.sort();
// console.log(arr);

// arr.sort((a, b) => a - b);
// console.log(arr);

// arr.sort((a, b) => b - a);
// console.log(arr);

// arr.sort((a, b) => {
//     if (a > b) {
//         return 1;
//     } else if (a < b) {
//         return -1;
//     } else {
//         return 0;
//     }
// });
console.log(arr);
arr.sort(function(a, b) {
    return a - b;
});
console.log(arr);