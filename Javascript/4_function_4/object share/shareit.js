function person(name, age) {
    let obj = Object.create(person.prototype);
    obj.name = name;
    obj.age = age;
    return obj;
}

person.prototype = {
    eat: function() {
        console.log("Person is eating");
    },
    sleep: function() {
        console.log("Person is sleeping");
    },
    walk: function() {
        console.log("Person is walking");
    }
}

const person1 = person("John", 30);
person1.country = "USA";
person1.city = "New York";
console.log(person1.name);
person1.eat();
person1.sleep();
person1.walk();

const person2 = person("Jane", 25);
person2.country = "UK";
person2.city = "London";
console.log(person2.name);
person2.eat();
person2.sleep();
person2.walk();
