// const add = (a, b) => a + b;
// console.log(add(1, 2));

// const add = (a, b) => {
//     return a + b;
// };
// console.log(add(1, 2));
// var javaScript = {
//     name: "JavaScript",
//     version: 2022,
//     libraries: ["React", "Angular", "Vue"],
    // print: function () {
    //     console.log("this print", this);
    //     this.libraries.forEach(function (library) { // this problem solve by arrow function
    //         console.log("'this' for each", this);
    //         console.log(this.name, library);
    //     });
    // }
    // print: function () { // normal function this keyword changed other wise self = this
        // var self = this;
        // this.libraries.forEach(function (library) {
        //     console.log(self.name, library);
        // });
//         this.libraries.forEach((library) => { // arrow function ignore this keyword
//             console.log(this.name, library);
//         });
//     }
// }
// javaScript.print();

var search = document.getElementById("search");
var result = document.getElementById("result");
var typing = document.getElementById("typing");
// function show() {
//     result.innerHTML = "Result " + this.value;
    // setTimeout(function () {
    //     typing.innerHTML = "Typing " + this.value;
    // }, 1000);
//     setTimeout(() => {
//         typing.innerHTML = "Typing " + this.value;
//     }, 1000);
// }

// search.addEventListener("keyup", show);

search.addEventListener("keyup", (e) => {
    result.innerHTML = "Result " + e.target.value;
    setTimeout(() => {
        typing.innerHTML = "Typing " + e.target.value;
    }, 2000);
});