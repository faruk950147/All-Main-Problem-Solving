// function stopWatch() {
//     let count = 0;
//     return function () {
//         count++;
//         return count;
//     }
// }
// var watch = stopWatch();
// console.dir(watch);

// function stopWatch() {
//     var timeStart = Date.now();
//     return function () {
//         return Date.now() - timeStart;
//     }
// }
// var watch = stopWatch();
// console.dir(watch);

function stopWatch() {
    var timeStart = Date.now();
    function getDelay() {
        console.log(Date.now() - timeStart);
        // return Date.now() - timeStart;
    }
    return getDelay;
}
var timer = stopWatch();
for (let i = 0; i < 1000000; i++) {
    var watch = Math.random() * 1000000;
}
console.dir(timer);
timer();


