
arr = [1, 2, 3, 4, 5];
// console.log(arr.length); // Output: 5

// let Length = 0;

// while (arr[Length] !== undefined) {
//     Length++;
// }
// console.log(Length); // Output: 5

// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
//     arr[i] = arr[i] * 2;
// }
// console.log(arr);
// sum = 0;    
// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
//     sum += arr[i];
// }
// console.log(sum);

// for (let i = 0; i < arr.length; i++) {
//     if (arr[i] % 2 == 0) {
//         console.log(arr[i] + " is even");
//     }
//     else {
//         console.log(arr[i] + " is odd");
//     }
// }

// found = 5
// for (let i = 0; i < arr.length; i++) {
//     if (arr[i] == found) {
//         console.log("Found" + found + "at index " + i);
//         break;
//     }else {
//         console.log("Not Found " + i);
//     }
    
// }
// console.log(arr)
// arr[0]=0
// arr.push(1)
// arr.unshift(2)
// arr.pop(0)
// arr.splice(0,1, 0)
// arr.splice(1, 0)
// console.log(arr)

arr1 =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
console.log(arr1)
console.log(arr1[0][1])
console.log(arr1[1][2])
console.log(arr1[2][0])

for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr1[i].length; j++) {
        console.log(arr1[i][j]);
    }
}












arr3 = [
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
]
console.log(arr3)
console.log(arr3[0][1][2])
console.log(arr3[1][2][1])

for (let i = 0; i < arr3.length; i++) {
    for (let j = 0; j < arr3[i].length; j++) {
        for (let k = 0; k < arr3[i][j].length; k++) {
            console.log(arr3[i][j][k]);
        }
    }
}
