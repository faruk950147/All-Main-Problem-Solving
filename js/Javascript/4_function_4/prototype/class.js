class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    eat() {
        console.log("Person is eating");
    }
    sleep() {
        console.log("Person is sleeping");
    }
    walk() {
        console.log("Person is walking");
    }
}

const person1 = new Person("John", 30);
person1.country = "USA";
person1.city = "New York";
console.log(person1.name);
person1.eat();
person1.sleep();
person1.walk();

const person2 = new Person("Jane", 25);
person2.country = "UK";
person2.city = "London";
console.log(person2.name);
person2.eat();
person2.sleep();
person2.walk();