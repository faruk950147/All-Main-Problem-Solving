// str = "Hello, World!";
// sym = Symbol("Hello World");
// console.log(str);
// console.log(sym);
// console.log(typeof str);
// console.log(typeof sym);

sym2 = Symbol("I'm a symbol 1");
sym3 = Symbol("I'm a symbol 2");
// console.log(sym2);
// console.log(sym3);
// console.log(sym2 === sym3);
// console.log(sym2 == sym3);
// var obj = {
//     [sym2]: "I'm a symbol 1",
//     [sym3]: "I'm a symbol 2"
// };
// console.log(obj);
// console.log(obj[sym2]);
// console.log(obj[sym3]);

// var obj = {
//     name: "John",
//     age: 30,
//     // symbol property is not iterable
//     [sym2]: "I'm a symbol 1",
//     [sym3]: "I'm a symbol 2"
// };
// obj[Symbol("founder")] = "Faruk";
// console.log(Object.keys(obj));
// console.log(obj[sym2]);
// console.log(obj[sym3]);
// console.log(obj.name);
// console.log(obj.age);

// for (let key in obj) {
//     console.log(key);
// }
// console.log(Object.keys(obj));
// console.log(Object.values(obj));
// console.log(Object.entries(obj));

// // symbol property is iterable
// console.log(Object.getOwnPropertySymbols(obj));
// console.log(Object.getPrototypeOf(obj));
// console.log(Object.getPrototypeOf(obj) === Object.prototype);

// // symbol property is iterable
// console.log(Object.getOwnPropertyNames(obj));
// console.log(Object.getOwnPropertySymbols(obj));
// console.log(Object.getPrototypeOf(obj));
// console.log(Object.getPrototypeOf(obj) === Object.prototype);

includes = Symbol("includes is iterable and returns boolean");
Array.prototype[includes] = (searchElement) => {
    console.log("this is array property");
    // return this.indexOf(searchElement) !== -1;
};
var arr = [1, 2, 3, 4, 5];
// console.log(arr.includes(3));
console.log(arr[includes](3));
arr[includes](6);


