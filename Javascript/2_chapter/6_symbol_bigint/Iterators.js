// arr = [1, 2, 3, 4, 5];
// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
// }

// Obj={
//     name:"John",
//     age:30,
//     city:"New York"
// }
// for (let key in Obj) { // of is not iterable not in symbol.iterable symbol
//     console.log(key);
// }

// let entries = Object.entries(Obj);
// console.log(entries);
// for (let i = 0; i < entries.length; i++) {
//     console.log(entries[i][0], entries[i][1]);
// }

let arr = [1, 2, 3, 4, 5];
let iterator = arr[Symbol.iterator]();
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());