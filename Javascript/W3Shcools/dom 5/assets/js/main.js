let myWindow;
const width = document.getElementById('width');
const height = document.getElementById('height');

//  show width and height of the window
width.innerHTML = "Width: " + window.innerWidth;
height.innerHTML = "Height: " + window.innerHeight;

function openWindow() {
    myWindow = window.open("https://www.w3schools.com", "_blank", "width=400,height=400");
}

function closeWindow() {
    myWindow.close();
}

