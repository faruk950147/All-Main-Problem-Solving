var func = function () {
    
}
// inside in master object all built-in function are stored 
// in built-in function we can add our function using prototype
// js master object is Object.prototype 
// eikhan thekei js built-in function er moddhe theke ase
Object.prototype.Faruk = function () {
    console.log("I am Faruk");
};

var obj = {};
obj.Faruk();