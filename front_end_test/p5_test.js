function setup() {
  var canvasDiv = document.getElementById("myCanvas");
  var width = canvasDiv.offsetWidth;
  var height = canvasDiv.offsetHeight;
  var sketchCanvas = createCanvas(width, windowHeight);
  sketchCanvas.parent("myCanvas");
}

function draw() {
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}

function windowResized() {
  console.log("true");
  var canvasDiv = document.getElementById("myCanvas");
  var width = canvasDiv.offsetWidth;
  var height = canvasDiv.offsetHeight;
  resizeCanvas(width, height);
}
