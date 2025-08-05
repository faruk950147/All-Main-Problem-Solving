const captain = {
    name: "LKD",
    age: 30,
    city: "Bangladesh"
};

function person(name, age) {
    let person = Object.create(captain);
    person.name = name;
    person.age = age;
    return person;
}

const person1 = person("John", 30);
const person2 = person("Jane", 25);
person1.city = "USA";
person2.city = "UK";
console.log(person1.city);
console.log(person2.city);
    