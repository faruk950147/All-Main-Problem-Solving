// // ******************************* while loop in JavaScript ******************************
// let i = 0;
// while (i < 5) {
//     console.log(i);
//     i++;
// }

// // ******************************* do while loop in JavaScript ******************************
// let j = 0;
// do {
//     console.log(j);
//     j++;
// } while (j < 5);

// // ******************************* for loop in JavaScript ******************************
// for (let k = 0; k < 5; k++) {
//     console.log(k);
// }

// // ******************************* break and continue in JavaScript ******************************
// for (let k = 0; k < 5; k++) {
//     if (k == 3) {
//         break;
//     }
//     console.log(k);
// }
    
// for (let k = 0; k < 5; k++) {
//     if (k == 3) {
//         continue;
//     }
//     console.log(k);
// }       

// // ******************************* nested loop in JavaScript ******************************
// for (let k = 0; k < 5; k++) {
//     for (let l = 0; l < 5; l++) {
//         console.log(k, l);
//     }
// }

// // ******************************* switch case in JavaScript ******************************
// let day = 3;


// function arrayMax(arr) {
//     let max = arr[0];
//     for (let i = 1; i < arr.length; i++) {
//         if (arr[i] > max) {
//             max = arr[i];
//         }
//     }
//     return max;
// }
// console.log(arrayMax([1, 2, 3, 4, 5]));

function arrayMax(arr) {
    let len = arr.length;
    let max = arr[len - 1];
    while (len--) {
        if (arr[len] > max) {
            max = arr[len];
        }
    }
    return max;
}
console.log(arrayMax([1, 2, 3, 4, 5]));