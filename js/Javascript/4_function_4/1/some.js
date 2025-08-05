// function display(data) {
//     console.log(data);
// }

// function calculator(arr) {
//     let sum = 0;
//     for(let i=0;i<arr.length;i++) {
//         sum += arr[i];
//     }
//     return sum;
// }
// // let result = calculator([1,2,3,4,5]);
// // display(result);

function some(data) {
    // console.log(data);
    return data;
}

function calculator(arr,callback) {
    let sum = 0;
    for(let i=0;i<arr.length;i++) {
        sum += arr[i];
    }
    if(callback) callback(sum);
    console.log("Addition");     
    return sum;  
}
calculator([1,2,3,4,5],some);