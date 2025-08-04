var rect = {
    width: 10,
    height: 20,
    // Anonyms function
    draw: function() {
        console.log('Drawing rectangle', this.width, this.height);
    },
    // Named function anonymous function
    calculateArea: function() {
        return this.width * this.height;
    },
    // Named function anonymous function
    calculateRange: function() {
        return this.width + this.height;
    }
};
var message = rect.draw();
var area = rect.calculateArea();
var range = rect.calculateRange();

console.log(message);
console.log(area);
console.log(range);

