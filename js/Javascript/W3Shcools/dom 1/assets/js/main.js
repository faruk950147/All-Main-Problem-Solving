// // select element
// const heading = document.getElementById("heading");
// heading.innerHTML = "I'm from javascript!";

// const para = document.getElementsByClassName("para");
// para[0].innerHTML = "I'm from javascript!";

// const span = document.getElementsByTagName("span");
// span[0].innerHTML = "I'm from javascript!";

// const btn = document.querySelector("#btn");


// // apply css
// heading.style.color = "red";
// heading.style.backgroundColor = "yellow";
// heading.style.fontSize = "20px";
// heading.style.padding = "10px";
// para[0].style.color = "green";
// para[0].style.backgroundColor = "yellow";
// para[0].style.fontSize = "20px";
// para[0].style.padding = "10px";
// span[0].style.color = "blue";
// span[0].style.backgroundColor = "yellow";
// span[0].style.fontSize = "20px";
// span[0].style.padding = "10px";

// btn.addEventListener("click", () => {
//     console.log("clicked");
//     heading.style.color = "blue";
//     para[0].style.color = "blue";
//     span[0].style.color = "blue";
// });

//// add attribute
// heading.setAttribute("class", "heading");
// para[0].setAttribute("class", "para");
// span[0].setAttribute("class", "span");

// // remove attribute
// heading.removeAttribute("class");
// para[0].removeAttribute("class");
// span[0].removeAttribute("class");

// // get attribute
// console.log(heading.getAttribute("class"));
// console.log(para[0].getAttribute("class"));
// console.log(span[0].getAttribute("class"));

// // get text content
// console.log(heading.textContent);
// console.log(para[0].textContent);
// console.log(span[0].textContent);   
demo = document.getElementById("demo");
const form = document.forms["form"];
const img = document.getElementById("img");

let text = "";
for (let i = 0; i < form.length; i++) {
    text += form.elements[i].value + "\n"; // elements[i] is the input element attribute
}
form.addEventListener("submit", (e) => {
    e.preventDefault();
    demo.innerHTML = text;
    img.src = "assets/2.jpg";
});

function validateForm() {
    // const name = document.getElementById("name").value;
    // const email = document.getElementById("email").value;
    // const password = document.getElementById("password").value;
    const name = form.name.value;
    const email = form.email.value;
    const password = form.password.value;
    if (name == "") {
        alert("Name is required");
        return false;
    }
    if (email == "") {
        alert("Email is required");
        return false;
    }
    if (password == "") {
        alert("Password is required");
        return false;
    }
    return true;
}
