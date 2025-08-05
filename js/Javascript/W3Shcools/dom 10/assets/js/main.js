const table = document.querySelector(".table");
const btn = document.getElementById("btn");
btn.addEventListener("click", function () {
    fetch("assets/js/data.json")
        .then((response) => response.json())
        .then((data) => {
            table.innerHTML += `<tr>
                <td>${data[0].name}</td>
                <td>${data[0].age}</td>
                <td>${data[0].city}</td>
            </tr>`;
        });
});
