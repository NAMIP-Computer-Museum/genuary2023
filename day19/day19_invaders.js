// genuary2023
day
19
black & white
// under
GPLv3
// based
on
Fernando
Jerez @ ferjerez3d
//  # genuary2022 Day 3. Space (Invaders)

let
S, P, A, C, E, m;
let
dc, dl, di, xt, yt;

function
generate(m, fc)
{
    let
even = (fc % 2) == 0
if (m == 36)
m = 67;
let
line = int(m / 9);
randomSeed(line + 1);

C = 100 + m % 9 * 80; // center
if (m < 36)
{
    C = C + dc * 14;
if ((3 - line) < ((fc + 3) % 4))
C = C + 14 * di;
} else {
    C = C + abs(fc % 30 - 15) * 30 - 110;
}

if (m == 67) P=9; else P=4; // last one
for (E=0;++E < 32 * (int(m / 67)+1);){
S=E % P * 7;
A=int(E / P) * 7+50+line * 90;

if (m < 36) A=A+dl * 20;

if ((int(E / P) > 5) & & even & & (m < 36)) random(2);
if (random(2) < 1){
rect(C+S, A, 7, 7);
rect(C-S, A, 7, 7);
}
}
}

function
setup()
{
    createCanvas(1000, 1000);
frameRate(5);
dc = 1;
dl = 0;
di = 1;
yt = 0;
}

function
draw()
{
    background(0);
if (frameCount < 20)
return;

noStroke();
for (let m=0;m < 37; m++){
    generate(m, frameCount);
}

// tir
if (yt < 0) {
yt=600;
xt=C;
} else {
yt=yt-60;
}
rect(xt, yt, 7, 20);

print(frameCount, dc, dl);
if (frameCount % 4 == 0) {
dc=dc+di;
if (dc == 8) {di=-1; dl=dl+1;}
if (dc == 0) {di=1;  dl=dl+1;}
}
}