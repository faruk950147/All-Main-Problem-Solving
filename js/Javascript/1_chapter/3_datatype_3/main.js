// ******************************* datatype in JavaScript ******************************
// File: 1_chapter/datatype_3/main.js
// datatype in JavaScript types of two types
// 1. Primitive Data Types
// number
// string
// boolean
// undefined
// null
// symbol
// bigint
// 2. Non-Primitive Data Types
// object
// array
// function
// date
// regexp
// map
// set
// weakmap
// weakset  

// ******************************** primitive Data Types ********************************
// Primitive data types are the most basic data types in JavaScript. They are immutable and represent
// Primitive Data Types
// 1. String
let name = "John Doe"; // String
// 2. Number
let age = 30; // Number
// 3. Boolean
let isEmployed = true; // Boolean
// 4. Undefined
let address; // Undefined
// 5. Null
let salary = null; // Null
// 6. Symbol (ES6)
let uniqueId = Symbol("id"); // Symbol
// 7. BigInt (ES11)
let bigNumber = BigInt(123456789012345678901234567890); // BigInt
// ******************************** non-primitive Data Types ********************************
// Non-primitive data types are more complex and can hold collections of values or more complex entities
// Non-Primitive Data Types
// 1. Object
let person = {
    name: "John Doe",
    age: 30,
    isEmployed: true,
    address: {
        city: "New York",
        country: "USA"
    }
}; // Object
// 2. Array
let numbers = [1, 2, 3, 4, 5]; // Array
// 3. Function
function greet() {
    console.log("Hello, World!");
} // Function
// 4. Date
let currentDate = new Date(); // Date
// 5. RegExp
let regex = /ab+c/; // Regular Expression
// 6. Map (ES6)
let map = new Map();
map.set("key1", "value1");
map.set("key2", "value2"); // Map
// 7. Set (ES6)
let set = new Set();
set.add(1);
set.add(2);
set.add(3); // Set
// 8. WeakMap (ES6)
let weakMap = new WeakMap();
let obj1 = {};
let obj2 = {};
weakMap.set(obj1, "value1");
weakMap.set(obj2, "value2"); // WeakMap
// 9. WeakSet (ES6)
let weakSet = new WeakSet();

// ************************************ Displaying Data Types **********************************
console.log("Primitive Data Types:");       
console.log("String:", typeof name);
console.log("Number:", typeof age);             
console.log("Boolean:", typeof isEmployed);
console.log("Undefined:", typeof address);
console.log("Null:", typeof salary);
console.log("Symbol:", typeof uniqueId);
console.log("BigInt:", typeof bigNumber);
console.log("\nNon-Primitive Data Types:");
console.log("Object:", typeof person);
console.log("Array:", typeof numbers);
console.log("Function:", typeof greet);
console.log("Date:", typeof currentDate);
console.log("RegExp:", typeof regex);
console.log("Map:", typeof map);
console.log("Set:", typeof set);
console.log("WeakMap:", typeof weakMap);
console.log("WeakSet:", typeof weakSet);
// Displaying the values of the variables
console.log("\nValues of Primitive Data Types:");
console.log("Name:", name);
console.log("Age:", age);

