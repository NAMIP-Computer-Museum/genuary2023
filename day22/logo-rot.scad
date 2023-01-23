cl=200;
cw=10;
ch=20;
n=8;

// IBM font is Menin Blue
// should install for all users
// for HAL: Fog Sans style outline

module stripes() {
for(i=[0:n-1]) {
  translate([0,i*cw*2,0])
    cube([cl,cw,ch]);
}
}

module IBM() {
translate([10,5,-10])
//rotate([45,0,0])
linear_extrude(50)
text( "I B M",size=20,font="MeninBlue:style=Normal" , $fn=50);
}

module HAL() {
translate([5,35,5])
rotate([90,0,0]) {
linear_extrude(40)
text( "H A L" ,size=20,font="Fog Sans:style=Outline" , $fn=50);
translate([74,10,0])
cylinder(d=14,h=40,$fn=50);
}    
}

//Arial Black:style=Bold

module build() {
difference(){
  cube([90,30,30]);
  HAL();
  IBM();
}
}

translate([-45,-15,-15])
build();