let arr = [1, 2, 3, 4, 5];
console.log(arr);           // full array print
console.log(arr.length);    // 5 (array length)
console.log(arr[0]);        // 1 (first element)
console.log(arr[1]);        // 2 (second element)
console.log(arr[2]);        // 3 (third element)
console.log(arr[3]);        // 4 (fourth element)
console.log(arr[4]);        // 5 (fifth element)

let set = new Set([1,2,3,4,5]);
console.log(set);           // Set(5) {1, 2, 3, 4, 5}
console.log(set.size);      // 5
console.log(set.has(3));    // true

set.add(6);                 // add new item
console.log(set);           // Set(6) {1, 2, 3, 4, 5, 6}

set.delete(3);              // delete item
console.log(set);           // Set(5) {1, 2, 4, 5, 6}



let obj = {name: "John", age: 30};
console.log(obj);           // full object print

// property access
console.log(obj.name);      // John
console.log(obj.age);       // 30

// add new property
obj.city = "New York";
obj["country"] = "USA";
console.log(obj);

// update property
obj["isEmployed"] = true;
obj["salary"] = 5000;
console.log(obj);

// Nested object create and add
obj["address"] = {street: "123 Main St", city: "New York", zip: "10001"};
obj["address"]["country"] = "USA";
obj["address"]["isEmployed"] = true;
obj["address"]["salary"] = 5000;

// nested object এর nested object
obj["address"]["address"] = {street: "123 Main St", city: "New York", zip: "10001"};
obj["address"]["address"]["country"] = "USA";
obj["address"]["address"]["isEmployed"] = true;
obj["address"]["address"]["salary"] = 5000;

// more nested
obj["address"]["address"]["address"] = {street: "123 Main St", city: "New York", zip: "10001"};
console.log(obj);

