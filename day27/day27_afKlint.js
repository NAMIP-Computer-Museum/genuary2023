// genuary 23 - day 27 - In the style of Hilma Af Klint
// GPLv3

let N=71;
let P=20;
var art,art2;
var cpos;
var mpos;
var pg;
var w2;
var h2;
var inv;
var n,m;

function initArt() {
  art=createGraphics(width, height);

  let we0=w2*1.2;
  let we1=2*w2/3;
  let we2=w2/3;

  art.noStroke();

//  cirk(w2,h2,we0,"#175d62","#aa779e",1);

// body
  art.fill("#175d62")
  art.ellipse(w2,h2,we0,we0);
//  art.fill("#a6432a");
//  art.arc(w2,h2,300,300,PI/2-PI/4,PI/2+PI/4);
//  art.fill("#175d62")
//  art.arc(w2,h2,250,250,PI/2-PI/4,PI/2+PI/4);
  ark(art,w2,h2,250,300,PI/2-PI/4,PI/2+PI/4,"#aa779e","#175d62");

// eye
  art.fill("#fff7a1")
  art.ellipse(w2,h2,we1,we1);
//  cirk(w2,h2,we1,"black","#fff7a1",-1)

// pupil
  art.fill("black");
  art.ellipse(w2,h2,we2,we2);
//  art.fill("#86283f");
//  art.strokeWeight(0.8);
//  art.stroke("#aa779e");
//  art.arc(ft(20,22),ft(14,19),ft(15,7),ft(20,17),0,ft(1.5,2.0),CHORD);
//  art.arc(220,190,70,170,-20,20,CHORD);
//   art.arc(ft(11,22),ft(7.5,19),ft(15,7),ft(20,17),0,ft(1.5,2.0),CHORD);
}

function setup() {
  createCanvas(600,600);
  w2=width/2;
  h2=height/2;
  cpos=0;
  mpos=100;
  inv=false;
  n=(N-1)/2;
  m=P;

  initArt();

  var img = createImage(w2,height);
  img.copy(art, 0, 0, w2, height, 0, 0, w2, height);
  art2=changeArt(img,0);

  frameRate(15);
}

function ark(pg,cx,cy,r1,r2,a1,a2,cf,cb)  {
    pg.fill(cf);
    pg.arc(cx,cy,r2,r2,a1,a2);
    pg.fill(cb);
    pg.arc(cx,cy,r1,r1,a1,a2);
}

function cirk(cx,cy,r,col1,col2,dir) {
  art.fill(col1);
  art.arc(cx,cy,r,r,-PI/2,3*PI/2);
  art.fill(col2);
  art.arc(cx,cy,r,r,-PI/2+dir*pg*PI,PI/2);

}

function ft(a,b) {
  if (cpos<0) return a;
  let pg=cpos/mpos;
  let noise=random(pg*(1-pg)*10);
  let res=a*(1-pg)+b*pg+noise;
  return res;
}

function changeArt(img,p) {
    // Load the pixels
    img.loadPixels();

    // Loop through the pixels X and Y
    for (let y = 0; y < img.height; y++) {
      for (let x = 0; x < img.width; x++) {

        // Calculate the pixel index
        const index = (y * img.width + x) * 4;

        // Get the red, green, and blue values
        const r = img.pixels[index + 0];
        const g = img.pixels[index + 1];
        const b = img.pixels[index + 2];

        // Invert the colors
        img.pixels[index + 0] = int(r*p+(255 - r)*(1-p));
        img.pixels[index + 1] = int(g*p+(255 - g)*(1-p));
        img.pixels[index + 2] = int(b*p+(255 - b)*(1-p));
      }
    }
    img.updatePixels();
  return img;
}

function draw() {

  noSmooth();
  pg=cpos/mpos;

  this.background("#b52a31");

  let wb1=w2*1.35;
  let wb2=w2*1.5;
  ark(this,w2,h2,wb1,wb2,PI+0.2,PI+1.4,"#7d4841","#b52a31");
  ark(this,w2,h2,0,wb2,PI+0.2,PI+0.35,"#7d4841","#b52a31");
  ark(this,w2,h2,wb1,wb2,PI-1.4,PI-0.2,"#7d4841","#b52a31");
  ark(this,w2,h2,0,wb2,PI-0.35,PI-0.2,"#7d4841","#b52a31");
  ark(this,w2,h2,wb1,wb2,0.2,1.4,"#7d4841","#b52a31");
  ark(this,w2,h2,0,wb2,0.2,0.35,"#7d4841","#b52a31");
  ark(this,w2,h2,wb1,wb2,-1.4,-0.2,"#7d4841","#b52a31");
  ark(this,w2,h2,0,wb2,-0.35,-0.2,"#7d4841","#b52a31");

  let p=(n%N)/(N-1);
  if (!inv) p=1-p;

  var img = createImage(w2,height);
  image(art, 0, 0, width, height);
  image(art2, 0, 0, w2, height);

  if (p<0.5)  {
    img.copy(art, w2, 0, w2, height, 0, 0, w2, height);
    changeArt(img,0);
    image(img, w2, 0, w2*(1-p*2), height);
  } else {
    img.copy(art, 0, 0, w2, height, 0, 0, w2, height);
    changeArt(img,1);
    let ww=w2*(p*2-1);
    if (ww>0) image(img, width*(1-p), 0, ww, height);
//    image(img,0,0,w2,height);
  }

  let nm=n%N;
//  print(nm,m,p);
  if (m>0) {
    m=m-1;
    return;
  }
  n=n+1;

  if (nm+1==int((N-1)/2)) {
    m=P;
    return;
  }

  if (nm==(N-1)) {
    m=P;
    inv=!inv;
    return;
  }

}