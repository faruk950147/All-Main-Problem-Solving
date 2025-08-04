function observer() {
    this.subscribers = [];
}

observer.prototype.subscribe = function (fn) {
    this.subscribers.push(fn);
}

const observer = new observer();
observer.subscribe(() => {
    console.log("Click");
});
