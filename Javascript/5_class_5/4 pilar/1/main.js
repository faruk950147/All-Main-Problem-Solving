function abtraction(width, height) {
    this.width = width;
    this.height = height;
    this.draw = function() {
        console.log('Drawing');
    }   
}
    
var rect = new abtraction(10, 20);
rect.draw();
