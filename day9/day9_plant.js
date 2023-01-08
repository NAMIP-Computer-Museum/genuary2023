// voxel trees - genuary 2023 - day 9
// GPLv3

let SIZE=1000;
let altitude = -0.2;
let voxelSize = 12;
let zoom = 200;
let tab = [];
//p5.disableFriendlyErrors = true;

class Vox {
  constructor(x,y,z,c) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.c = c;
  }
}

function createLine1(v0,v1) {
   var dx = v1.x - v0.x;
   var dy = v1.y - v0.y;
   var dz = v1 .z- v0.z;
   var deltaErrorY = abs(dy / dx);
   var deltaErrorZ = abs(dz / dx);
   var errorY = 0;
   var errorZ = 0;
   var y = v0.y;
   var z = v0.z;
   var col = "sienna";
   console.log("ici",v0.x);
   for (var x = v0.x; x<v1.x; x += voxelSize) {
     console.log(x,y,z);
     var vox=new Vox(x,y,z,col);
     append(tab,vox);
     errorY += deltaErrorY;
     while (errorY >= 0.5) {
         y += sign(dy);
         errorY --;
     }
     errorZ += deltaErrorZ;
     while (errorZ >= 0.5) {
         z += sign(dz);
         errorZ --;
     }
   }
}

function createLine(v0,v1,c) {
   var x0=v0.x;
   var y0=v0.y;
   var z0=v0.z;
   var x1=v1.x;
   var y1=v1.y;
   var z1=v1.z;
   var dx = abs(x1-x0), sx = x0<x1 ? 1 : -1;
   var dy = abs(y1-y0), sy = y0<y1 ? 1 : -1;
   var dz = abs(z1-z0), sz = z0<z1 ? 1 : -1;
   var dm = max(dx,dy,dz), i = dm; /* maximum difference */
   x1 = y1 = z1 = dm/2; /* error offset */

   for(;;) {  /* loop */
     var vox=new Vox(x0,y0,z0,c);
     append(tab,vox);
     if (i-- == 0) break;
     x1 -= dx; if (x1 < 0) { x1 += dm; x0 += sx; }
     y1 -= dy; if (y1 < 0) { y1 += dm; y0 += sy; }
     z1 -= dz; if (z1 < 0) { z1 += dm; z0 += sz; }
   }
}

function setup() {
  createCanvas(SIZE, SIZE, WEBGL);
  noStroke();
//debugMode();
  ortho(-width/2-100, width/2+100, -height/2-100, height/2+100,-100,2000);
  camera(-400,-400,-400);
  init();
}

function vround(x) {
  return round(x/voxelSize)*voxelSize;
}

function tree(x,y,z,h) {
  var pb=new p5.Vector(x,y,z);
  var ps=new p5.Vector(x,y-h,z);
  createLine(pb,ps,"sienna")
  var nl=random(round(h/70),round(h/30));
  var nb=random(8,18);
  var r=random(h/6,h/3);
  var pbt=new p5.Vector(0,0,0);
  var pbe=new p5.Vector(0,0,0);
  var xp=0;
  var yp=0;
  var zp=0;
  var h2=4*h/6;
  for(var l=0; l<nl; l++) {
    pbt.set(x,vround(y-h+l*h2/nl),z)
    yp=vround(y-h+(l+1)*h2/nl);
//    console.log(pbt);
//    console.log(yp);
    for(var a=0.0; a<6.28; a+=6.28/nb) {
      xp=vround(x+r*(l+1)/nl*sin(a));
      zp=vround(z+r*(l+1)/nl*cos(a));
      pbe.set(xp,yp,zp);
//      console.log(pbe);
//      console.log(xp);
      createLine(pbe,pbt,"green")
    }
  }
}

function init() {

  for (var x = 0; x < SIZE; x += voxelSize) {
    for (var z = 0; z < SIZE; z += voxelSize) {
      var value = Math.max(
					noise(
						(1 / zoom * x),
						(1 / zoom * z)) +
				  altitude,
				  0
			);
      var c=getColor(value);
      for (var y = 0; y<=floor(value*10); y++) {
        var vox=new Vox(x-SIZE/2,-y*voxelSize,z-SIZE/2,c);
        append(tab,vox);
      }
    }
  }
  /*
  var a=new p5.Vector(0,0,0);
  var b=new p5.Vector(0,150,0);
  var col="sienna";
  console.log(a,b,col);
  createLine(a,b,col); */
  //tree(0,0,0,200)
}

function draw() {
  frameRate(4);

  background('white');
  orbitControl(2, 2, 0.1);
  ambientLight(150, 150, 150);
  directionalLight(255, 255, 255, 0.5, 1, -1);

  for (var i = 0; i < tab.length; i++) {
    if (box.x==-1000) continue;

    fill(tab[i].c);
	push();
    // Note: by default "Up" is negative in the y axis
	translate(tab[i].x, tab[i].y, tab[i].z);
	box(voxelSize);
	pop();
  }

  if (frameCount<3) return;
  if (frameCount>40) return;

  console.log(frameCount);
  tree(vround(random(-SIZE/2.2,SIZE/2.2)),-20,vround(random(-SIZE/2.2,SIZE/2.2)),vround(random(60,300)));
}

function getColor(value) {
	for (let ix = 0; ix < gradientStops.length; ix++) {
		if (value <= gradientStops[ix]) {
			return gradientColors[ix];
		}
	}

	// default
	return 'white';
}

function getIndex(value) {
	for (let ix = 0; ix < gradientStops.length; ix++) {
		if (value <= gradientStops[ix]) {
			return ix
		}
	}

	// default
	return -1;
}

let gradientColors = [
	'lightseagreen',
	'lightgreen',
	'limegreen',
	'forestgreen',
	'green',
	'peru',
	'sienna',
	'gray',
	'gainsboro'
];
let gradientStops = [
	0,
	0.02,
	0.04,
	0.1,
	0.2,
	0.4,
	0.6,
	0.8,
	1
];
