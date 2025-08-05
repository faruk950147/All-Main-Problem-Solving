const personMethods = {
    eat: function () {
        console.log("Person is eating");
    },
    sleep: function () {
        console.log("Person is sleeping");
    },
    walk: function () {
        console.log("Person is walking");
    }
};
    
function person(name, age) {
    let person = {}
    person.name = name;
    person.age = age;
    person.eat = personMethods.eat;
    person.sleep = personMethods.sleep;
    person.walk = personMethods.walk;
    return person;
}

const person1 = person("John", 30);
const person2 = person("Jane", 25);
person1.eat();
person2.sleep();
person1.walk();