class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    get getter() {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
    set setter(value) {
        this.name = value;
    }
    static staticMethod() {
        console.log("This is a static method.");
    }
    static staticMethod2() {
        console.log("This is a static method2.");
    }
}
class Cricketer extends Person {
    constructor(name, age, role, country) {
        super(name, age);
        this.role = role;
        this.country = country;
    }
    team() {
        console.log(`${this.name} is from ${this.country}`);
    }
    play() {
        console.log(`${this.name} is playing ${this.role}`);
    }
    run() {
        console.log(`${this.name} is running`);
    }
    out() {
        console.log(`${this.name} is out`);
    }
    ball() {
        console.log(`${this.name} is bowling`);
    }
    bat() {
        console.log(`${this.name} is batting`);
    }
    toss(role) {
        console.log(`${this.name} is tossing ${role}`);
    }
}
const person1 = new Person("John", 30);
person1.getter;
person1.setter = "Jane";
console.log(person1.getter);
Person.staticMethod();
Person.staticMethod2();
const cricketer1 = new Cricketer("Virat", 32, "Batsman", "India");
cricketer1.team();
cricketer1.play();
cricketer1.run();
cricketer1.out();
cricketer1.ball();
cricketer1.bat();
cricketer1.toss("bat");
