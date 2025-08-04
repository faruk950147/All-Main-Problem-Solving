// function greets(msg) {
//     return function (name) {
//         console.log(msg + " " + name);
//     }
// }

// const greet = greets("Hello");
// greet("John");
    
// function greets(msg) {
//     function greetings(name) {
//         return msg + " " + name;
//     }
//     return greetings;
// }

// const gm = greets("Good Morning");
// const gm2 = greets("Good Afternoon");
// const gm3 = greets("Good Evening");
// const gm4 = greets("Good Night");
// console.log(gm("John"));
// console.log(gm2("John"));
// console.log(gm3("John"));
// console.log(gm4("John"));

// function base(x) {
//     function pow(n) {
//         let result = 1;
//         for (let i = 0; i < n; i++) {
//             result *= n;
//         }
//         return result;
//     }
//     return pow;
// }

// const base2 = base(2);
// console.log(base2(3));

// function base(x) {
//     return function (n) {
//         let result = 1;
//         for (let i = 0; i < n; i++) {
//             result *= x;
//         }
//         return result;
//     }
// }

// const base10 = base(10);
// console.log(base10(2));


function base(x) {
    return function pow(n) {
        let result = 1;
        for (let i = 0; i < x; i++) {
            result *= n;
        }
        return result;
    }
}

const base10 = base(10);
console.log(base10(2));


