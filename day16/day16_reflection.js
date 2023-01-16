// Genuary2023 day 16 - reflection of a reflection
// licence GPLv3

let img
let FC=1
let NC=5
let N=100/FC // divider
let zoom=[]
let col=[]
let fact=0.2
let grow=1.2

function setup() {
  createCanvas(400, 400)
  img = loadImage('retro.png')
  colorMode(HSB,100,100,100)
  imageMode(CENTER)
  rectMode(CENTER)
  zoom[0]=0.6
  col[0]=0
  for(let i=1; i<NC; i++) {
    zoom[i]=zoom[i-1]*fact
    col[i]=col[i-1]+10
  }
}

function myUpdate() {
  for(let i=0; i<NC; i++) {
    zoom[i]=zoom[i]*grow
  }
  if (zoom[0]<10) return;

  // update
  for(let i=0; i<NC-1; i++) {
    zoom[i]=zoom[i+1]
    col[i]=col[i+1]
  }
  zoom[NC-1]=zoom[NC-2]*fact
  col[NC-1]=(col[NC-2]+10)%100
}

function draw() {
  frameRate(10)
  let n=frameCount%N
  background(col[0],100,100)
  for(let i=0; i<NC; i++) {
    image(img, width/2, height/2+zoom[i]*75, width*zoom[i], height*zoom[i])
    fill(col[i+1],100,100);
    noStroke()
    rect(width/2, height/2+zoom[i]*15, 222*zoom[i], 160*zoom[i])
  }
  myUpdate()
}