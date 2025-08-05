// ******************************* es6 or es 6 *******************************

// ******************************* let and const *******************************
let a = 10;
const b = 20;
console.log(a, b);

// ******************************* arrow function *******************************
const add = (a, b) => a + b;
console.log(add(1, 2));

// ******************************* template literal *******************************
const name = "John";
const age = 30;
console.log(`My name is ${name} and I am ${age} years old.`);

// ******************************* spread operator *******************************
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5, 6];
console.log(arr2);

// ******************************* rest operator *******************************
const sum = (...args) => args.reduce((a, b) => a + b, 0);
console.log(sum(1, 2, 3, 4, 5));

// ******************************* default parameter *******************************
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
console.log(greet("John"));

// ******************************* class *******************************
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
}
console.log(new Person("John", 30));

// ******************************* map *******************************
const map = new Map();
map.set("name", "John");
map.set("age", 30);
console.log(map);

// ******************************* set *******************************
const set = new Set();
set.add(1);
set.add(2);
set.add(3);
console.log(set);

// ******************************* weak map *******************************
const weakMap = new WeakMap();
const obj1 = {};
const obj2 = {};
weakMap.set(obj1, "value1");
weakMap.set(obj2, "value2");
console.log(weakMap);

// ******************************* weak set *******************************
const weakSet = new WeakSet();
const obj3 = {};
const obj4 = {};
weakSet.add(obj3);
weakSet.add(obj4);
console.log(weakSet);

// ******************************* symbol *******************************
const sym = Symbol("id");
console.log(sym);

// ******************************* bigint *******************************
const bigInt = BigInt(123456789012345678901234567890);
console.log(bigInt);

// ******************************* promise *******************************
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Success!");
    }, 1000);
});
promise.then((result) => console.log(result));

// ******************************* generator *******************************
function* generator() {
    yield 1;
    yield 2;
    yield 3;
}
const gen = generator();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

// ******************************* proxy *******************************
const handler = {
    get: function(target, prop) {
        if (prop in target) {
            return target[prop];
        } else {
            throw new Error("Property not found");
        }
    }
};
const obj = {name: "John", age: 30};
const proxy = new Proxy(obj, handler);
console.log(proxy.name);
console.log(proxy.age);
console.log(proxy.salary);

// ******************************* iterator *******************************
const iterator = [1, 2, 3][Symbol.iterator]();
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());

// ******************************* async/await *******************************
async function asyncFunction() {
    return "Hello, World!";
}
asyncFunction().then((result) => console.log(result));

// ******************************* template literal *******************************
// const name = "John";
// const age = 30;
// console.log(`My name is ${name} and I am ${age} years old.`);

