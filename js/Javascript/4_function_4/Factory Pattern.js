var factoryFunction = function (width, height) {
    return {
        width: width,
        height: height,
        draw: function () {
            this.printProperties();
            console.log("draw");
            console.log(this);
        },
        printProperties: function () {
            console.log("Width: " + this.width);
            console.log("Height: " + this.height);
        }
    }   
}

var rect1 = factoryFunction(10, 20);
rect1.draw();

var rect2 = factoryFunction(30, 40);
rect2.draw();

var rect3 = factoryFunction(50, 60);
rect3.draw();
