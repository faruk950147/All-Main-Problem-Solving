// syntax
// /pattern/modifiers/ flags

// modifiers
// i, g, m

// i - case insensitive
// g - global
// m - multiline

// methods
// test()
// exec()
// match()
// search()
// replace()
// split()

let str = "Hello, World!";
let regex = /World/i;
console.log(regex.test(str));
console.log(regex.exec(str));
console.log(str.match(regex));
console.log(str.search(regex));
console.log(str.replace(regex, "Universe"));
console.log(str.split(regex));

