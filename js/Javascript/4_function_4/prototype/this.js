// rule of this
// 1. implicit binding
// 2. explicit binding
// 3. new binding
// 4. default binding or global binding or window binding

// 1. implicit binding
// function implicitBinding() {
//     console.log(this);
// }
// implicitBinding();

// var person = {
//     name: "John",
//     age: 30,
//     play: function() {
//         console.log(this.name + " is playing");
//     }
// }
// person.play();

// var person = function(name, age) {
//     return {
//         name: name,
//         age: age,
//         play: function() {
//             console.log(this.name + " is playing");
//         }
//     }
// }
// person().play();


// var person = function(name, age) {
//     return {
//         name: name,
//         age: age,
//         play: function() {
//             console.log(this.name + " is playing");
//         },
//         father: {
//             name: name,
//             age: age,
//             print: function() {
//                 console.log(this.name + " is father");
//             }
//         }

//     }
// }
// person("John", 30).play();
// person("John", 30).father.print();


var person = {
    name: "John",
    age: 30,
    play: function() {
        console.log(this.name + " is playing");
    }
}

// 2. explicit binding
function explicitBinding() {
    console.log(this);
}
explicitBinding.call(person);


// 3. new binding
function newBinding() {
    console.log(this);
}
newBinding();

// 4. default binding or global binding or window binding
function defaultBinding() {
    console.log(this);
}
defaultBinding();
