class rect {
    constructor(width, height) {
        this.width = width;
        this.height = height;   
    }
    draw() {
        console.log('Drawing rectangle', this.width, this.height);
    }
    calculateArea() {
        return this.width * this.height;
    }
    calculateRange() {
        return this.width + this.height;
    }
}

var obj = new rect(10, 20);
obj.draw();
console.log(obj.calculateArea());
console.log(obj.calculateRange());