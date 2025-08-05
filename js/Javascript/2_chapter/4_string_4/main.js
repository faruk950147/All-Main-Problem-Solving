// str = "Hello, World!";
// console.log("Original String:", str);
// // Convert to uppercase
// let upperStr = str.toUpperCase();
// console.log("Uppercase String:", upperStr);
// // // Convert to lowercase
// // let lowerStr = str.toLowerCase();
// // console.log("Lowercase String:", lowerStr);
let str1 = "Hello, World!";
// console.log(str1.split(" ")); // if u want to split space then use " " else use "" and any other character
// join is in array method not in string method
console.log(str1.join(" A ")); // is in array if u want to join space then use " " else use "" and any other character
// console.log(str1.length); // to find the length of the string
// console.log(str1.slice(0, 5));     // "Hello"
//console.log(str1.slice(7));        // "World!"
// console.log(str1.slice(-6));       // "World!"
// console.log(str1.slice(-6, -1));   // "World"
// console.log(str.slice(7, 12));    // "World"
// console.log(str.slice(0, -1));    // "Hello, World"
// let str3 = "Hello, World!";

// console.log(str.substring(0, 5));  // "Hello"
// console.log(str.substring(7));     // "World!"
// console.log(str.substring(7, 12)); // "World"


// let str = "Hello";

// let reversed = str.split("").reverse().join("");
// console.log(reversed);  // "olleH"


// // Convert to sentence case
// function toSentenceCase(str) {
//     return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
// }

// // Convert to title case    
// function toTitleCase(str) {
//     return str.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
// }
// let titleStr = toTitleCase(str);
// console.log("Title Case String:", titleStr);
// // Convert to camel case
// function toCamelCase(str) { 
//     return str.toLowerCase().split(' ').map((word, index) => {
//         if (index === 0) return word;
//         return word.charAt(0).toUpperCase() + word.slice(1);
//     }).join('');
// }
// let camelStr = toCamelCase(str);
// console.log("Camel Case String:", camelStr);
// // Convert to snake case
// function toSnakeCase(str) {
//     return str.toLowerCase().split(' ').join('_');
// }   
// let snakeStr = toSnakeCase(str);
// console.log("Snake Case String:", snakeStr);
// // Convert to kebab case
// function toKebabCase(str) {
//     return str.toLowerCase().split(' ').join('-');
// }   
// let kebabStr = toKebabCase(str);
// console.log("Kebab Case String:", kebabStr);
// // Convert to Pascal case
// function toPascalCase(str) {
//     return str.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
// }
// let pascalStr = toPascalCase(str);
// console.log("Pascal Case String:", pascalStr);
// // Convert to reverse case
// function toReverseCase(str) {
//     return str.split('').reverse().join('');
// }
// let reverseStr = toReverseCase(str);
// console.log("Reversed String:", reverseStr);
// // Convert to alternating case
// function toAlternatingCase(str) {
//     return str.split('').map((char, index) => {
//         return index % 2 === 0 ? char.toUpperCase() : char.toLowerCase();
//     }).join('');
// }
// let alternatingStr = toAlternatingCase(str);
// console.log("Alternating Case String:", alternatingStr);
// // Convert to leet case
// function toLeetCase(str) {
//     const leetMap = {
//         'A': '4', 'B': '8', 'C': '<', 'D': '|)', 'E': '3', 'F': '|=', 
//         'G': '9', 'H': '#', 'I': '1', 'J': '_|', 'K': '|<', 'L': '|_', 
//         'M': '/\\/\\', 'N': '^/', 'O': '0', 'P': '|*', 'Q': '(,)', 
//         'R': '|2', 'S': '$', 'T': '+', 'U': '|_|', 'V': '\\/', 
//         'W': '\\/\\/', 'X': '%', 'Y': '`/', 'Z': '2'
//     };
//     return str.toUpperCase().split('').map(char => leetMap[char] || char).join('');
// }   
// let leetStr = toLeetCase(str);
// console.log("Leet Case String:", leetStr);
// // Convert to Morse code
// function toMorseCode(str) {
//     const morseMap = {
//         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
//         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
//         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
//         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
//         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
//         'Z': '--..', 
//         '0': '-----', '1': '.----', '2': '..---', 
//         '3': '...--', '4': '....-', 
//         '5': '.....', '6': '-....', 
//         '7': '--...', '8': "---..", 
//         '9': "----."
//     };
//     return str.toUpperCase().split('').map(char => morseMap[char] || char).join(' ');
// }
// let morseStr = toMorseCode(str);
// console.log("Morse Code String:", morseStr);
// // Convert to binary
// function toBinary(str) {
//     return str.split('').map(char => {
//         return char.charCodeAt(0).toString(2).padStart(8, '0');
//     }).join(' ');
// }
// let binaryStr = toBinary(str);
// console.log("Binary String:", binaryStr);
// // Convert to hexadecimal
// function toHexadecimal(str) {
//     return str.split('').map(char => {
//         return char.charCodeAt(0).toString(16).padStart(2, '0');
//     }).join(' ');
// }
// let hexStr = toHexadecimal(str);
// console.log("Hexadecimal String:", hexStr);
// // Convert to octal
// function toOctal(str) {
//     return str.split('').map(char => {
//         return char.charCodeAt(0).toString(8).padStart(3, '0');
//     }).join(' ');
// }
// let octalStr = toOctal(str);
// console.log("Octal String:", octalStr);
// // Convert to base64
// function toBase64(str) {
//     return btoa(unescape(encodeURIComponent(str)));
// }
// let base64Str = toBase64(str);
// console.log("Base64 String:", base64Str);
// // Convert to URL encoding
// function toURLEncoding(str) {
//     return encodeURIComponent(str);
// }
// let urlEncodedStr = toURLEncoding(str);
// console.log("URL Encoded String:", urlEncodedStr);
// // Convert to HTML entities
// function toHTMLEntities(str) {
//     const htmlEntitiesMap = {
//         '&': '&amp;',
//         '<': '&lt;',
//         '>': '&gt;',
//         '"': '&quot;',
//         "'": '&#39;'
//     };
//     return str.split('').map(char => htmlEntitiesMap[char] || char).join('');
// }
// let htmlEntitiesStr = toHTMLEntities(str);
// console.log("HTML Entities String:", htmlEntitiesStr);
// // Convert to JSON
// function toJSON(str) {
//     return JSON.stringify({ text: str });
// }   
// let jsonStr = toJSON(str);
// console.log("JSON String:", jsonStr);
// // Convert to XML
// function toXML(str) {
//     return `<text>${toHTMLEntities(str)}</text>`;
// }
// let xmlStr = toXML(str);
// console.log("XML String:", xmlStr);

// // Convert to CSV
// function toCSV(str) {
//     return `"${str.replace(/"/g, '""')}"`;
// }   
// let csvStr = toCSV(str);
// console.log("CSV String:", csvStr);
// // Convert to YAML
// function toYAML(str) {
//     return `text: "${str.replace(/"/g, '\\"')}"`;
// }
// let yamlStr = toYAML(str);
// console.log("YAML String:", yamlStr);
// // Convert to INI
// function toINI(str) {
//     return `[text]\nvalue="${str.replace(/"/g, '\\"')}"`;
// }   
// let iniStr = toINI(str);
// console.log("INI String:", iniStr);
// // Convert to Plain Text
// function toPlainText(str) {
//     return str.replace(/<[^>]*>/g, '').replace(/&[^;]+;/g, '');
// }   
// let plainTextStr = toPlainText(str);
// console.log("Plain Text String:", plainTextStr);
// // Convert to JavaScript String
// function toJavaScriptString(str) {
//     return `"${str.replace(/"/g, '\\"')}"`;
// }
// let jsStr = toJavaScriptString(str);
// console.log("JavaScript String:", jsStr);
// // Convert to Python String
// function toPythonString(str) {
//     return `'${str.replace(/'/g, "\\'")}'`;
// }
// let pythonStr = toPythonString(str);
// console.log("Python String:", pythonStr);
// // Convert to Ruby String
// function toRubyString(str) {
//     return `"${str.replace(/"/g, '\\"')}"`;
// }   
// let rubyStr = toRubyString(str);
// console.log("Ruby String:", rubyStr);
