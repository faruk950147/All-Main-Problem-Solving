// JavaScript Display Possibilities
// JavaScript can "display" data in different ways:

// Writing into an HTML element, using innerHTML or innerText.
// Writing into the HTML output using document.write().
// Writing into an alert box, using window.alert().
// Writing into the browser console, using console.log().
// Using innerHTML
// To access an HTML element, you can use the document.getElementById(id) method.

// Use the id attribute to identify the HTML element.

// Then use the innerHTML property to change the HTML content of the HTML element:
// document.getElementById("demo").innerHTML = "<h2>Hello World InnerHTML</h2>";

// document.getElementById("demo").innerText = "Hello World InnerText";

// // Using document.write()

// var btn = document.getElementById("btn");
// btn.onclick = function () {
//     document.write("Hello World Document Write");
// }

// Using window.alert()
window.alert("Hello World Window Alert");
// Using console.log()
console.log("Hello World Console Log");
