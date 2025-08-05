// decision make 5
// File: 1_chapter/5_decision_make_5/main.js
// ********************************* Decision Making in JavaScript ******************************
// if (5 > 10) {  //     console.log("5 is greater than 10");
// } else if (5 < 10) {  //     console.log("5 is less than 10");
// } else {  //     console.log("5 is equal to 10");    
// }
// ********************************* Switch Case in JavaScript ******************************
// switch (5) {
//     case 1:  //         console.log("5 is equal to 1");
//         break;
//     case 5:  //         console.log("5 is equal to 5");
//         break;
//     case 10:  //         console.log("5 is equal to 10");
//         break;
//     default:  //         console.log("5 is not equal to 1, 5 or 10");
//         console.log("5 is not equal to 1, 5 or 10");
//         break;
// }
// ********************************* Ternary Operator in JavaScript ******************************
// const result = (5 > 10) ? "5 is greater than 10"
//                  : (5 < 10) ? "5 is less than 10"
//                  : "5 is equal to 10";   
// console.log(result);
// ********************************* Logical Operators in JavaScript ****************************** 
// const a = true;
// const b = false;
// console.log(a && b);  // Logical AND
// console.log(a || b);  // Logical OR
// console.log(!a);     // Logical NOT
// ********************************* Short-Circuit Evaluation in JavaScript ******************************  
// const x = 5;
// const y = 10;    
// const result = (x > 0) && (y < 20) ? "Both conditions are true" : "At least one condition is false";
// console.log(result);     
// ********************************* Nested If Statements in JavaScript ******************************
// const age = 20;
// if (age >= 18) {
//     console.log("You are an adult.");    
//     if (age >= 21) {
//         console.log("You can drink alcohol in the US.");
//     } else {
//         console.log("You cannot drink alcohol in the US.");
//     }    
// } else {
//     console.log("You are a minor.");
// }
// ********************************* Using Functions for Decision Making in JavaScript ******************************   
// function checkNumber(num) {
//     if (num > 0) {
//         return "The number is positive.";
//     } else if (num < 0) {
//         return "The number is negative.";
//     } else { \
//         return "The number is zero.";
//     }
// }
// console.log(checkNumber(5));  // The number is positive. 
// console.log(checkNumber(-3)); // The number is negative.
// console.log(checkNumber(0));  // The number is zero.
// ********************************* Using Loops with Decision Making in JavaScript ******************************
// for (let i = 1; i <= 5; i++) {
//     if (i % 2 === 0) {
//         console.log(i + " is even.");
//     } else {
//         console.log(i + " is odd.");
//     }
// }

// ********************************* Using Arrays with Decision Making in JavaScript ******************************
// const numbers = [1, 2, 3, 4, 5];
// numbers.forEach(num => {
//     if (num % 2 === 0) { 
//         console.log(num + " is even.");
//     } else {
//         console.log(num + " is odd.");
//     }
// });
// ********************************* Using Objects with Decision Making in JavaScript ******************************
// const person = {
//     name: "John",
//     age: 30, 
//     isStudent: false
// };
// if (person.age >= 18) {
//     console.log(person.name + " is an adult.");  
//     if (person.isStudent) {
//         console.log(person.name + " is a student.");
//     } else {
//         console.log(person.name + " is not a student."); 
//     }
// } else {
//     console.log(person.name + " is a minor.");
// }

// ********************************* Using Async/Await with Decision Making in JavaScript ******************************
// const checkAgeAsync = async (age) => {
//     try {    
//         const message = await checkAge(age);
//         console.log(message);  // You are an adult.  
//     } catch (error) {
//         console.log(error);  // You are a minor.
//     }
// };
// checkAgeAsync(20);  // You are an adult.
// checkAgeAsync(16);  // You are a minor.
// ********************************* Using Error Handling with Decision Making in JavaScript ******************************
// const divide = (a, b) => {
//     if (b === 0) {
//         throw new Error("Cannot divide by zero.");
//     }
//     return a / b;    
// };
// try {    
//     console.log(divide(10, 2));  // 5
//     console.log(divide(10, 0));  // Error: Cannot divide by zero.
// } catch (error) {
//     console.log(error.message);  // Cannot divide by zero.
// }
// ********************************* Using Conditional (Ternary) Operator with Decision Making in JavaScript ******************************     
// const age = 18;
// const canVote = (age >= 18) ? "You can vote." : "You cannot vote.";
// console.log(canVote);  // You can vote.
// ********************************* Using Logical Operators with Decision Making in JavaScript ******************************
// const isAdult = true;
// const hasPermission = false;
// const canAccess = isAdult || hasPermission;
// console.log(canAccess);  // true
// ********************************* Using Short-Circuit Evaluation with Decision Making in JavaScript ******************************
// const isLoggedIn = true;
// const isAdmin = false;   
// const canAccessAdminPanel = isLoggedIn && isAdmin;
// console.log(canAccessAdminPanel);  // false
// ********************************* Using Nested If Statements with Decision Making in JavaScript ******************************
// const score = 85;    
// if (score >= 90) {
//     console.log("Grade: A");
// } else if (score >= 80) {
//     console.log("Grade: B"); 
// } else if (score >= 70) {
//     console.log("Grade: C");
// } else if (score >= 60) {    
//     console.log("Grade: D");
// } else {
//     console.log("Grade: F");
// }
// ********************************* Using Functions for Decision Making in JavaScript ******************************
// function isEven(num) {
//     return num % 2 === 0;
// }
// console.log(isEven(4));  // true
// console.log(isEven(5));  // false    
// }
// ********************************* Using Loops with Decision Making in JavaScript ******************************  
// for (let i = 1; i <= 10; i++) {
//     if (i % 2 === 0) {
//         console.log(i + " is even.");
//     } else { 
//         console.log(i + " is odd.");
//     }    
// }

// ********************************* Using Arrays with Decision Making in JavaScript ******************************
// const fruits = ["apple", "banana", "cherry"];    
// fruits.forEach(fruit => {
//     if (fruit === "banana") {
//         console.log(fruit + " is my favorite fruit.");
//     } else {
//         console.log(fruit + " is not my favorite fruit.");
//     }
// });
// ********************************* Using Objects with Decision Making in JavaScript ******************************
// const car = {    
//     brand: "Toyota",
//     model: "Camry",
//     year: 2020
// };   
// if (car.year >= 2020) {
//     console.log(car.brand + " " + car.model + " is a new car.");
// } else {
//     console.log(car.brand + " " + car.model + " is an old car.");
// }
// }

// ********************************* Using Promises with Decision Making in JavaScript ******************************
// const checkAge = (age) => {  
//     return new Promise((resolve, reject) => {
//         if (age >= 18) {
//             resolve("You are an adult.");
//         } else {
//             reject("You are a minor.");
//         }
//     });
// };
// checkAge(20)
//     .then(message => console.log(message))  // You are an adult.
//     .catch(error => console.log(error));  // You are a minor.
// checkAge(16)
//     .then(message => console.log(message))  // You are an adult.
    // .catch(error => console.log(error));  // You
// are a minor.

// ********************************* Using Async/Await with Decision Making in JavaScript ******************************
// const fetchData = async () => {  
//     try {
//         const response = await fetch("https://api.example.com/data");
//         if (!response.ok) {
//             throw new Error("Network response was not ok");
//         }
//         const data = await response.json();
//         console.log(data);  // Process the data
//     } catch (error) {
//         console.error("There was a problem with the fetch operation:", error);
//     }    
// };
// fetchData();  // Call the async function to fetch data   

