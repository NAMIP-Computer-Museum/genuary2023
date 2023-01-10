var art;
var cpos;
var mpos;

function setup() {
  createCanvas(600,600);
  art=createGraphics(40, 40);
  cpos=-5;
  mpos=15;
}

function ft(a,b) {
  if (cpos<0) return a;
  let pg=cpos/mpos;
  let noise=random(pg*(1-pg)*10);
  let res=a*(1-pg)+b*pg+noise;
  return res;
}

function draw() {
  frameRate(1);
  noSmooth();
  print(cpos);

  art.noStroke();
  art.background("#b52a31");
//  art.background("#ba2d33");

  art.noStroke();
  art.fill("#7d4841");
  art.push();
  art.translate(ft(5,17),18);
  art.rotate(ft(0,-0.9));
  art.rect(0,0,15,2);
  art.pop();

  art.push();
  art.translate(7,20);
  art.rotate(ft(PI/2,-PI/2));
  art.rect(0,0,15,2);
  art.pop();

  art.push();
  art.translate(ft(5,10),ft(33,39));
  art.rotate(ft(0,-PI/2));
  art.rect(0,0,15,2);
  art.pop();

  art.push();
  art.translate(20,ft(20,25));
  art.rotate(ft(PI/2,1.0));
  art.rect(0,0,15,2);
  art.pop();

  art.fill("#175d62")
  art.ellipse(ft(30,15), ft(30,22), 20, 20);
  art.fill("#fff7a1")
  art.stroke("black");
  art.ellipse(ft(10,19), ft(10,16), 10, 10);
  art.fill("black");
  art.ellipse(ft(4,21), ft(37,17), 4, 4);
  art.fill("#86283f");
  art.strokeWeight(0.8);
  art.stroke("#aa779e");
//  art.arc(ft(20,22),ft(14,19),ft(15,7),ft(20,17),0,ft(1.5,2.0),CHORD);
  art.arc(ft(17,22),ft(15,19),ft(15,7),ft(20,17),0,ft(1.5,2.0),CHORD);
//   art.arc(ft(11,22),ft(7.5,19),ft(15,7),ft(20,17),0,ft(1.5,2.0),CHORD);

  image(art, 0, 0, width, height);

  cpos++;
  if (cpos>mpos) cpos=mpos;
}