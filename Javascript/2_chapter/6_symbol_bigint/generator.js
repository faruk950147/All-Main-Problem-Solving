// function* generator() {
//     yield 1;
//     yield 2;
//     yield 3;
// }
// let gen = generator();
// console.log(gen.next());
// console.log(gen.next());
// console.log(gen.next());
// console.log(gen.next());


obj={
    name:"John",
    age:30,
    city:"New York"
}
// Object.prototype[Symbol.iterator] = function* () {
//     const entries = Object.entries(this);
//     return {
//         next: function* () {
//             if (entries.length > 0) {
//                 yield entries.shift();
//             } else {
//                 return { done: true };
//             }
//         }
//     }
// }
// for (let key of obj) {
//     console.log(key);
// }


function* generator(obj) {
    const entries = Object.entries(obj);
    for (let i = 0; i < entries.length; i++) {
        yield entries[i];
    }
}

let gen = generator(obj);
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

