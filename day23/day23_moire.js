// genuary23 day 23 more moire
// GPLv3

let g1,g2,g3

function createCircle(dr,col) {
  let g=createGraphics(width*2,height*2);
  let w2=width
  let h2=height
  g.stroke(col)
  g.strokeWeight(1)
  g.noFill()
  for(let r=0;r<width*2;r+=dr){
    g.ellipse(w2,h2,r,r)
  }

  return g
}

function createGrid(dx,col) {
  let g=createGraphics(width*2,height*2);
  g.stroke(col)
  g.strokeWeight(1)
  g.noFill()
  for(let x=0;x<g.width;x+=dx){
    g.line(x,0,x,g.height)
  }
  for(let y=0;y<g.height;y+=dx){
    g.line(0,y,g.width,y)
  }
  return g

}

function setup() {
  createCanvas(600, 600);
  origin
//  rectMode(CENTER);

  g1=createCircle(5,color(255,0,0,170))
  g2=createCircle(5,color(255,0,0,170))
  g3=createGrid(2,color(255,140,0,170))
}

function draw() {
  frameRate(10)
  background(255)

  push()
  translate(width/2,height/2)
  scale((sin(frameCount/13)+2.4)*1.8)
  translate(-width/2,-height/2)
  image(g1,-width/2+sin(-frameCount/20)*50,-height/2+cos(-frameCount/10)*50)
  image(g2,-width/2+sin(PI+frameCount/10)*50,-height/2+cos(PI+frameCount/10)*50)


  pop();

  push()
//  translate(-width/2,-height/2)
//  rotate(frameCount/17)
  scale((sin(frameCount/19)+2.4)*1.5)
//  translate(width/2,height/2)
  image(g3,0,0)
  pop()

//  fill("black")
//  ellipse(0,0,20,20)
}