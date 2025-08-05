const btn = document.getElementById("btn");

function debounce(fn, delay) {
    let timeout;
    return function () {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            fn();
        }, delay);
    };
}
btn.addEventListener("click", debounce(() => {
    console.log("Click");
}, 1000));
