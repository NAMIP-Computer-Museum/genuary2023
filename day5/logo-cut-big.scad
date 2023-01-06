
z=20;
h=1.4;
g=0.3;
color=["blue","violet","red","orange","yellow","green"];

// TODO generate eslice from 1 to 6 and export as STL
eslice(1);
translate([0,0,4]) eslice(2);
translate([0,0,8]) eslice(3);
translate([0,0,12]) eslice(4);
translate([0,0,16]) eslice(5);
translate([0,0,20]) eslice(6);

module eslice(n) {
  if (n>1) {
    difference() {
      slice(n);
      hbox(n);
    }  
  } else slice(n);
  if (n<6) rbox(n);
// hbox(n+1);
}

module slice(n) {
  if (n<6) {
    intersection() {
      ibox(n);
      color(color[n-1]) apple();
    }
  } else {
    intersection() {
      ibox(n,4);
      color(color[5]) apple();
    }
  }
}

module apple() {
scale([z,0.5*z,z])
  rotate([90,0,0])
    translate([0,5.1,-2])
      import("3d_apple_logo_fixed.stl", convexity=3);
}

module ibox(n,f=1) {
translate([-5.5*z,-z,(n-1)*h*z])
  cube([11*z,11*z,h*z*f]);
}

module rbox(n) {
color(color[n])
translate([-3*z,0.35*z,+n*h*z-0.5])
  cube([6*z,h/4*z,h/4*z]);
}

module hbox(n) {
translate([-3*z-g,0.35*z-g,+(n-1)*h*z-0.5+g])
  cube([6*z+g*2,h/4*z+g*2,h/4*z]);
}


