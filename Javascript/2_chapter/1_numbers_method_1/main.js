

// *********************** Numbers in JavaScript ***********************
// JavaScript provides a set of built-in methods and properties for working with numbers.
// These methods and properties allow you to perform mathematical operations, check number types, and format numbers
// in various ways. Below is a comprehensive list of these methods and properties, along with examples of their usage.
// Note: JavaScript uses the IEEE 754 standard for representing numbers, which means all numbers    
// are stored as floating-point values. This can lead to precision issues with very large or very small numbers.
// Basic Arithmetic Operations
// JavaScript supports basic arithmetic operations such as addition, subtraction, multiplication, division, and modulus 

// ************************** Number Methods and Properties **************************
let isNaNValue = isNaN("Hello"); // Check if value is NaN
console.log("Is NaN:", isNaNValue);
let isFiniteValue = isFinite(10 / 0); // Check if value is finite
console.log("Is Finite:", isFiniteValue);
let isIntegerValue = Number.isInteger(10.5); // Check if value is an integer
console.log("Is Integer:", isIntegerValue);
let isSafeInteger = Number.isSafeInteger(9007199254740991); // Check if value is a safe integer
console.log("Is Safe Integer:", isSafeInteger);
let toFixedValue = (10.123456).toFixed(2); // Format number to fixed decimal places
console.log("To Fixed:", toFixedValue);
let toExponentialValue = (10).toExponential(2); // Format number in exponential notation
console.log("To Exponential:", toExponentialValue);
let toPrecisionValue = (10.123456).toPrecision(4); // Format number to specified precision
console.log("To Precision:", toPrecisionValue);
let toStringValue = (10).toString(); // Convert number to string
console.log("To String:", toStringValue);
let parseIntValue = parseInt("10.5"); // Parse string to integer
console.log("Parse Int:", parseIntValue);
let parseIntBase = parseInt("10", 10); // Parse string to integer with base
console.log("Parse Int with Base:", parseIntBase);
let parseFloatValue = parseFloat("10.5"); // Parse string to float
console.log("Parse Float:", parseFloatValue);
let numberValue = Number("10.5"); // Convert string to number
console.log("Number:", numberValue);
let parseIntHex = parseInt("0xF", 16); // Parse hexadecimal string
console.log("Parse Int Hex:", parseIntHex);
let parseIntBinary = parseInt("1010", 2); // Parse binary string
console.log("Parse Int Binary:", parseIntBinary);
let parseIntOctal = parseInt("12", 8); // Parse octal string
console.log("Parse Int Octal:", parseIntOctal);
let randomValue = Math.random(); // Generate a random number between 0 and 1
console.log("Random Value:", randomValue);
let randomInt = Math.floor(Math.random() * 100); // Generate a random integer between
console.log("Random Integer:", randomInt);
let maxValue = Number.MAX_VALUE; // Maximum representable number
console.log("Max Value:", maxValue);
let minValue = Number.MIN_VALUE; // Minimum representable number
console.log("Min Value:", minValue);
let epsilonValue = Number.EPSILON; // Smallest difference between two representable numbers
console.log("Epsilon Value:", epsilonValue);
// 0 and 99
let randomRange = Math.floor(Math.random() * (50 - 10 + 1)) + 10; // Generate a random integer between 10 and 50
console.log("Random Range (10 to 50):", randomRange);

let randomFloat = (Math.random() * 100).toFixed(2); // Generate a random float between 0 and 100 with two decimal places
console.log("Random Float (0 to 100):", randomFloat);
let randomSign = Math.random() < 0.5 ? -1 : 1; // Generate a random sign (-1 or 1)
console.log("Random Sign:", randomSign);
let randomSignedInt = randomSign * Math.floor(Math.random() * 100); // Generate a random signed integer between -99 and 99
console.log("Random Signed Integer (-99 to 99):", randomSignedInt);
let randomSignedFloat = randomSign * (Math.random() * 100).toFixed(2); // Generate a random signed float between -100 and 100 with two decimal places
console.log("Random Signed Float (-100 to 100):", randomSignedFloat);
// Math Methods
let piValue = Math.PI; // Value of π (pi)
console.log("Pi Value:", piValue);
let absValue = Math.abs(-10); // Absolute value
console.log("Absolute Value:", absValue);
let ceilValue = Math.ceil(10.1); // Round up to the nearest integer

let floorValue = Math.floor(10.9); // Round down to the nearest integer

let roundValue = Math.round(10.5); // Round to the nearest integer

let maxNumber = Math.max(10, 20, 30); // Maximum of a set of numbers

let minNumber = Math.min(10, 20, 30); // Minimum of a set of numbers

let sqrtValue = Math.sqrt(16); // Square root 

let powValue = Math.pow(2, 3); // Power (2 raised to the power of 3)

let logValue = Math.log(10); // Natural logarithm

let log10Value = Math.log10(100); // Base 10 logarithm

let expValue = Math.exp(2); // Exponential function (e raised to the power of 2)

let sinValue = Math.sin(Math.PI / 2); // Sine of an angle in radians

let cosValue = Math.cos(Math.PI); // Cosine of an angle in radians    

let tanValue = Math.tan(Math.PI / 4); // Tangent of an angle in radians

let asinValue = Math.asin(1); // Inverse sine (arcsine)

let acosValue = Math.acos(0); // Inverse cosine (arccosine)

let atanValue = Math.atan(1); // Inverse tangent (arctangent)

// Trigonometric functions in JavaScript use radians, not degrees.
// To convert degrees to radians, multiply by Math.PI / 180.        
// To convert radians to degrees, multiply by 180 / Math.PI.    
// Example of converting degrees to radians and vice versa
let degrees = 180;
let radians = degrees * (Math.PI / 180); // Convert degrees to radians
console.log("Radians:", radians);
let degreesFromRadians = radians * (180 / Math.PI); // Convert radians to degrees
console.log("Degrees:", degreesFromRadians);

let num1 = 10;
let num2 = 5;
let sum = num1 + num2; // Addition  
console.log("Sum:", sum);
let difference = num1 - num2; // Subtraction
console.log("Difference:", difference);
let product = num1 * num2; // Multiplication
console.log("Product:", product);
let quotient = num1 / num2; // Division
console.log("Quotient:", quotient);
let remainder = num1 % num2; // Modulus
console.log("Remainder:", remainder);
let exponent = num1 ** num2; // Exponentiation
console.log("Exponent:", exponent);
let increment = num1++; // Increment
console.log("Increment:", increment);
let decrement = num2--; // Decrement
console.log("Decrement:", decrement);
let isEqual = num1 === num2; // Strict equality check
console.log("Is Equal:", isEqual);
let isNotEqual = num1 !== num2; // Strict inequality check
console.log("Is Not Equal:", isNotEqual);
let isGreater = num1 > num2; // Greater than
console.log("Is Greater:", isGreater);
let isLess = num1 < num2; // Less than
console.log("Is Less:", isLess);
let isGreaterOrEqual = num1 >= num2; // Greater than or equal to
console.log("Is Greater or Equal:", isGreaterOrEqual);
let isLessOrEqual = num1 <= num2; // Less than or equal to
console.log("Is Less or Equal:", isLessOrEqual);
