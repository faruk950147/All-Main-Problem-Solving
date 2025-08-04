var Car = function (width, height) {
    this.width = width;
    this.height = height;
    this.draw = function () {
        console.log('Drawing rectangle', this.width, this.height);
    }
    this.printProperties = function () {
        console.log("Width: " + this.width);
        console.log("Height: " + this.height);
    }
}

var rect = new Car(10, 20);
rect.draw();
rect.printProperties();