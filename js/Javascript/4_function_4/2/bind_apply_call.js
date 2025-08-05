function display() {
    // this window
    console.log(this);
    console.log("Hello");
    // custom context bind apply call
    console.log(this.a + this.b);
}

// display();

display.bind({a: 10, b: 20})();
display.apply({a: 10, b: 20});
display.call({a: 10, b: 20});

display.bind({a: 10, b: 20}, 10, 20)();
display.apply({a: 10, b: 20}, [10, 20]);
display.call({a: 10, b: 20}, 10, 20);