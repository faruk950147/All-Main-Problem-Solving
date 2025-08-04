
// event listener
// addEventListener()

const btn = document.getElementById("btn");
const demo = document.getElementById("demo");

btn.addEventListener("click", function () {
    console.log("Hello World!");
    btn.style.backgroundColor = "red";
    btn.style.color = "white";
    btn.style.padding = "10px";
    btn.style.border = "none";
    btn.style.borderRadius = "5px";
    btn.style.cursor = "pointer";
    btn.style.fontSize = "20px";
    demo.style.color = "red";
});
