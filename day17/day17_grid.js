// genuary 2023 - day 17 - cponsard
// GPLv3

let N=11;
let BW=30;
let PP=10;
let D=-BW*(N/2.0-0.5);
let DEP=950;
let MAXF=130;
let px=0;
let py=0;
let pz=DEP;
let tx=0;
let ty=0;
let tz=0;
let ux=0;
let uy=1;
let uz=0;
let dx=0;
let dy=0;
let dz=-1;
let maxx=BW*N/2.0;
let maxy=maxx;
let maxz=maxx
let minx=-maxx;
let miny=-maxy;
let minz=-maxz;

function ft(a,b) {
  if (frameCount<30) return a;
  let pg=(frameCount-30)/(MAXF-30);
  if (pg>1.0) pg=1.0;
  let res=a*(1-pg)+b*pg;
  return res;
}

function setup() {
  createCanvas(800,600, WEBGL);
  perspective(PI/4,width/height,0.1,1100);
  camera(px,py,pz,tx,ty,tz,ux,uy,uz);
  colorMode(HSB, 100, 100, 100, 100);
  frameRate(5);
}

function computeTarget() {
  print("compute target")
  print("OLD",dx,dy,dz);
  ux=dx;
  uy=dy;
  uz=dz;
  if (abs(dx)>0.1) { dy=-dx; dx=0; }
  else if (abs(dy)>0.1) { dz=-dy; dy=0; }
  else if (abs(dz)>0.1) { dx=-dz; dz=0; }
  tx=px+2*BW*dx;
  ty=py+2*BW*dy;
  tz=pz+2*BW*dz;
  print("NEW",dx,dy,dz);
}

function progressTarget() {
}

function borg() {
  let ch,cs,cb;
  let col1;
  let col2;
  noFill();
  for(let i=0; i<N; i++) {
  for(let j=0; j<N; j++) {
  for(let k=0; k<N; k++) {
    ch=ft(i/N*100,30+i/N*15);
    cs=ft(20+j/N*80,60+j/N*40);
    cb=ft(20+k/N*80,20+j/N*20);
    col1=color(ch,cs,cb,100);
    col2=color(ch,cs,cb,50);
    strokeWeight(10);
    stroke(col1);
    fill(col2);
    push();
    translate(D+i*BW,D+j*BW,D+k*BW);
    box(BW);
    pop();
  }}}

//  fill(255,0,0);
//  push();
//  translate(D+2*BW,D+2*BW,D+2*BW);
//  box(BW);
//  pop();

}

function draw() {
   camera(px,py,pz,tx,ty,tz,ux,uy,uz);

  background(0);

  push();
  rotateX(frameCount/10);
  rotateY(frameCount/20);
  borg();
  pop();

  // update
//if (frameCount%10==0) print(frameCount,"P:",px,py,pz,"D:",dx,dy,dz,"T:",tx,ty,tz, DEP);
/*  if ((dx>0) && (px>tx)) computeTarget();
  if ((dx<0) && (px<tx)) computeTarget();
  if ((dy>0) && (py>ty)) computeTarget();
  if ((dy<0) && (py<ty)) computeTarget();
  if ((dz>0) && (pz>tz)) computeTarget();
  if ((dz<0) && (pz<tz)) computeTarget();

  px=px+PP*dx
  py=py+PP*dy;
  pz=pz+PP*dz;
  */
  if ((frameCount>MAXF) && (pz<DEP)) { pz=pz+PP; }
  else if (pz>maxz-BW*2) pz=pz-PP;

}