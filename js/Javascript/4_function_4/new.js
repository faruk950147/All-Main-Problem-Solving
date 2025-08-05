function New(constructor) {
    let obj = {};
    Object.setPrototypeOf(obj, constructor.prototype);
    let argsArray = Array.prototype.slice.apply(arguments, 1);
    constructor.apply(obj, argsArray.slice(1));
    return obj;
}

var rect = New(Car, 10, 20);
rect.draw();