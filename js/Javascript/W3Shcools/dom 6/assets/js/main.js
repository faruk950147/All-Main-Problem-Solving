// window screen
const width = document.getElementById("width");
const height = document.getElementById("height");
const availWidth = document.getElementById("availWidth");
const availHeight = document.getElementById("availHeight");
const colorDepth = document.getElementById("colorDepth");
const pixelDepth = document.getElementById("pixelDepth");
const screenX = document.getElementById("screenX");
const screenY = document.getElementById("screenY");
const x = document.getElementById("x");
const y = document.getElementById("y");

width.innerHTML = window.screen.width;
height.innerHTML = window.screen.height;
availWidth.innerHTML = window.screen.availWidth;
availHeight.innerHTML = window.screen.availHeight;
colorDepth.innerHTML = window.screen.colorDepth;
pixelDepth.innerHTML = window.screen.pixelDepth;
screenX.innerHTML = window.screenX;
screenY.innerHTML = window.screenY;
x.innerHTML = window.screenX;
y.innerHTML = window.screenY;
