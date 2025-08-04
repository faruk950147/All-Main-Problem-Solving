const car = {
    brand: "Toyota",
    model: "Camry",
    year: 2020,
    color: "black",
    weight: 1500,
    start: function() {
        this.turnOn();
        console.log("Engine started");
    },
    stop: function() {
        console.log("Engine stopped");
    },
    turnOn: function() {
        console.log("Car is on");
    },
    turnOff: function() {
        console.log("Car is off");
    }
};
console.log(car.brand);
car.start();
car.stop();
car.turnOn();
car.turnOff();
