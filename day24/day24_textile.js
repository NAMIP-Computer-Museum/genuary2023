// genuary23 day 24 textile
// GPLv3

let N=14;
let N2=N/2;
let M=10;
let c,w,h,m;
let img;

function knit(x,y,col) {
  col[3]=220;
  col2=color(col[0]*0.95,col[1]*0.95,col[2]*0.95,220);
  stroke(col2);
  strokeWeight(N2);
  line(x,y,x+N2-2,y+N-2);
  stroke(col);
  line(x+N-4,y,x+N2-2,y+N-2);
}

function preload() {
  img = loadImage("mario-peach.png");
}

function setup() {
  frameRate(20);
  createCanvas(img.width*N,img.height*N);
  print(img.width,img.height);
//  colorMode(HSB,100);
  c=0;
  w=int(width/N);
  h=int(height/N);
  m=w*h;
  background("beige");
  frameRate(20);
}

function draw() {
  if (frameCount<20) return;
  if (c==m) return;
//  for(let y=0; y<height; y+=N) {
//    for(let x=0; x<width; x+=N) {
//      let col=color(y/h*100,100,100);
  for(let i=0;i<M;i++){
  let x=c%w;
  let y=int(c/w);
  let col=img.get(x,y);
  knit(x*N,y*N,col);
  c+=1;
//  if (c==m) { c=0; background(255);}
  }
}