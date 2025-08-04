function apiCall(url) {
    fetch(url)
    .then(res => res.json())
    .then(res => {
        let show = document.getElementById("show");
        let data = JSON.stringify(res);
        show.innerHTML = data;
    })
    .catch(error => console.log(error));
}
apiCall("https://jsonplaceholder.typicode.com/posts");