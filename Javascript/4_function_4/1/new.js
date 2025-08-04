// new 4 work
// 1. empty object create
// 2. set prototype
// 3. call constructor
// 4. return object

// empty object create
const obj = new Object();
console.log(obj);

// set prototype
// Object.prototype.name = "Faruk";
// console.log(obj.name);

// call constructor
// function Person(name) {
//     this.name = name;
//     return this;
// }
// const person = new Person("Faruk");
// console.log(person.name);

// return object
// console.log(person);

class Person {
    constructor(name) {
        this.name = name;
    }
}
const person = new Person("Faruk");
console.log(person.name);