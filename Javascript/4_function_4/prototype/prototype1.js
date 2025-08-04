// Person is a constructor in person prototype
// Person is a constructor in person prototype
function Person(name, age) {
    // right now parent 
    this.name = name;
    this.age = age;
}
// Cricketer is a Person (inheritance) in cricketer prototype
function Cricketer(name, age, role, country) {
    // right now child
    Person.call(this);
    this.name = name;
    this.age = age;
    this.role = role;
    this.country = country;
}
// Person is a constructor in person prototype
Person.prototype = {
    play: function() {
        console.log(`${this.name} is playing`);
    },
    eat: function() {
        console.log(`${this.name} is eating`);
    },
    sleep: function() {
        console.log(`${this.name} is sleeping`);
    },
    walk: function() {
        console.log(`${this.name} is walking`);
    }
}
// Cricketer is a Person (inheritance) in cricketer prototype
Cricketer.prototype = Object.create(Person.prototype);
// Cricketer is a constructor in cricketer prototype override
Cricketer.prototype.constructor = Cricketer;
// Cricketer is a constructor in cricketer prototype override
Cricketer.prototype.toss = function(role) {
    console.log(`${this.name} is tossing ${role}`);
}

let tamim = new Cricketer("Tamim", 30, "Opener Batter", "Bangladesh");
tamim.play();
tamim.toss("Right");
let shamim = new Cricketer("Shamim", 25, "All Rounder", "Bangladesh");
shamim.play();
shamim.toss("Left");
