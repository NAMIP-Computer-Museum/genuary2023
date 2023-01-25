// genuary23 day 25 Yayoi Kusama
// GPLv3

let N=10;
let tab=[];
let amiga;

function computeTexture(n,s) {
  img=createGraphics(200,200);
  img.background("red");
  img.noStroke();
  for(let i=0; i<n; i++) {
    let w=s/2+random(s/2);
    let h=20+random(20);
    let x=w/2+random(img.width-w);
    let y=h/2+random(img.height-h);
    img.fill("white");
    img.ellipse(x,y,w,w)
  }
  return img;
}

function mySphere(p,t) {
  print(t);
  if (t<15) return;

  push();
  translate(p[0],p[1],p[2]);
  rotateZ(random(2*PI));
//  scale(0.5+random(0.5),0.5+random(0.5),0.5+random(0.5));
  rotateX(random(2*PI));
  rotateY(random(2*PI));
  texture(tab[int(random(N))]);
  noStroke();
  sphere(t);
  pop();

  for(let i=0;i<10;i++) {
    let a=random(2*PI);
    let b=random(PI/2);
    let h=t*sin(b);
    let c=t*cos(b);
    let x=p[0]+c*sin(a);
    let z=p[2]+c*cos(a);
    let y=p[1]+h;
    mySphere([x,y,z],t/4);
  }
}

function preload() {
  amiga=loadImage("amiga.png");
}

function setup() {
  createCanvas(800, 800, WEBGL);
  perspective(PI/4,width/height,10,2000);
  camera(650,400,650,0,0,0,0,-1,0);
  noLoop();
  for(let i=0;i<N-1;i++) {
    tab[i]=computeTexture(15,20);
  }
  tab[N-1]=amiga;
}

function draw() {
  background(200,50,50);
  ambientLight(255, 255, 255);
  pointLight(255,255,255,700, 800, 600);
  directionalLight(255,255,255,0,-500,0);
  directionalLight(255,255,255,0,500,0);

  noFill();
  noStroke();

  push();
  texture(computeTexture(100,10))
  translate(500,500,0);
  plane(1000,1000);
  pop();

  push();
  texture(computeTexture(100,10))
  translate(0,500,500);
  rotateY(PI/2);
  plane(1000,1000);
  pop();

  push();
  texture(computeTexture(100,10))
  translate(500,0,500);
  rotateX(PI/2);
  plane(1000,1000);
  pop();

  let max=100;
  for(let i=0;i<15;i++) {
    let x=random(450);
    let z=random(450);
    let t=random(100-x/60-z/60);
    let y=t;
    let p=mySphere([x,y,z],t);
  }

}

// We use the key pressed function here
function keyPressed() {

  // If you hit the s key, save an image
  if (key == 's') {
    save("mySketch.png");
  }
}