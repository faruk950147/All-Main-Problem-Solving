
// This code demonstrates the use of different variable types in JavaScript
// It includes string, number, boolean, array, and object types


// var keyword allows for variable declaration and can be re-assigned


// ****************************** using var keyword variable declaration ******************************


// Using var to declare variables
// var a; var b; var name; var age; var isActive; var numbers; var person;

// ****************************** assigning values to variables ******************************
// a = 10; // number  
// b = 20; // number
// name = "John"; // string
// age = 30; // number
// isActive = true; // boolean
// numbers = [1, 2, 3, 4, 5]; // array
// person = { // object
//     firstName: "John",
//     lastName: "Doe",
//     age: 30,
//     isActive: true
// };
// ******************************* Displaying the values of the variables *************************
// console.log("Value of a: " + a);
// console.log("Value of b: " + b);
// console.log("Name: " + name);
// console.log("Age: " + age);
// console.log("Is Active: " + isActive);
// console.log("Numbers: " + numbers);
// console.log("Person: " + JSON.stringify(person));
// // Displaying the type of the variables
// console.log("Type of a: " + typeof a);  
// console.log("Type of b: " + typeof b);
// console.log("Type of name: " + typeof name);
// console.log("Type of age: " + typeof age);
// console.log("Type of isActive: " + typeof isActive);
// console.log("Type of numbers: " + typeof numbers);
// console.log("Type of person: " + typeof person);



// ******************************* using var keyword declaration and values assignment ******************************
// var name = "John";
// var age = 30;
// console.log(name + "is known as the 'JavaScript Developer' in the community.");
// console.log("His age is " + age + " years old.");

//******************************** using var keyword in allows re-assignment ******************************
// var name = "John";
// var age = 30;
// // console.log(name + " is known as the 'JavaScript Developer' in the community.");
// // console.log("His age is " + age + " years old.");


// // Re-assigning the variables
// name = "Jane";
// age = 25;
// // console.log(name + " is known as the 'JavaScript Developer' in the community.");
// // console.log("Her age is " + age + " years old.");

// // Re-assigning the variables again
// name = "Alice";
// age = 28;
// console.log(name + " is known as the 'JavaScript Developer' in the community.");
// console.log("Her age is " + age + " years old.");

// ****************************** using let keyword variable declaration and re-assignment not allows ******************************
// let keyword allows for variable declaration and can be re-assigned
// let a = 10; // number
// let b = 20; // number    
// let name = "John"; // string
// let age = 30; // number
// let isActive = true; // boolean
// let numbers = [1, 2, 3, 4, 5]; // array
// let person = { // object
//     firstName: "John",
//     lastName: "Doe",
//     age: 30,
//     isActive: true
// };

// ************************* using const keyword variable declaration and re-assignment *************************
// const keyword allows for variable declaration but does not allow re-assignment
// const pi = 3.14; // number
// const name = "John"; // string
// const isActive = true; // boolean
// const numbers = [1, 2, 3, 4, 5]; // array
// const person = { // object
//     firstName: "John",
//     lastName: "Doe",
//     age: 30,
//     isActive: true
// };
// // Displaying the values of the variables
// console.log("Value of pi: " + pi);                   

// console.log("Name: " + name);
// console.log("Is Active: " + isActive);
// console.log("Numbers: " + numbers);
// console.log("Person: " + JSON.stringify(person));

// ************************** multiple variable in single line *************************
// Using var to declare multiple variables in a single line
// var x = 10, y = 20, z = 30; // number
// console.log("Value of x: " + x);
// console.log("Value of y: " + y); 
// console.log("Value of z: " + z);
