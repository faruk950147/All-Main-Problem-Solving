// create element
// const para = document.createElement("p");
// const node = document.createTextNode("This is new.");
// para.appendChild(node);
// const element = document.getElementById("demo");
// element.appendChild(para);

// insert element
// const element2 = document.getElementById("demo");
// const p1 = document.getElementById("p1");
// element2.insertBefore(para, p1);

// remove element
// const parent = document.getElementById("demo");
// const child = document.getElementById("p1");
// parent.removeChild(child);

// replace element
// const parent = document.getElementById("demo");
// const child = document.getElementById("p1");
// const newChild = document.createElement("p");
// const node = document.createTextNode("This is new.");
// newChild.appendChild(node);
// parent.replaceChild(newChild, child);

// get element by tag name
// const element = document.getElementById("demo");
// const x = element.getElementsByTagName("p");
// console.log(x);

// html collection
console.dir(document.getElementById("demo").parentElement);

// node list
console.log(document.getElementById("demo").childNodes);

// node type
console.log(document.getElementById("demo").nodeType);

// node value
console.log(document.getElementById("demo").nodeValue);

// node name
console.log(document.getElementById("demo").nodeName);

// node parent
console.log(document.getElementById("demo").parentNode);

// node child
console.log(document.getElementById("demo").childNodes);

// node first child
console.log(document.getElementById("demo").firstChild);

// node last child
console.log(document.getElementById("demo").lastChild);

// node next sibling
console.log(document.getElementById("demo").nextSibling);

// node previous sibling
console.log(document.getElementById("demo").previousSibling);

// node next element sibling
console.log(document.getElementById("demo").nextElementSibling);

// node previous element sibling
console.log(document.getElementById("demo").previousElementSibling);
