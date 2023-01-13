// genuary2023 day 12 truchet tiles
// glv3

let cellSize = 50
let listCell = []
let SIZE=600
let n= SIZE/cellSize
let pi=0
let pj=0
let dir=0
let cs2=cellSize/2
let cs4=cellSize/4
let vcol1="red"
let vcol2="pink"

function randomBool() {
  return (random(100)>50)
}

function randomDir() {
  if (randomBool()) return 1
  return -1
}

function randomDir() {
  while(true) {
    r=floor(random(0,4))
    if (r==4) r=3
    if ((r+2)%4!=dir) return r // not opposite
  }
}

function setup() {
  createCanvas(SIZE,SIZE);
  angleMode(DEGREES)
  for(i=0;i<n;i+=1){
    listCell[i]=[]
    for(j=0;j<n;j+=1){
      listCell[i][j] = ((i+j)%2==0) //randomBool()
      if (listCell[i][j]) drawCellA(i,j)
      else drawCellB(i,j)
    }
  }
}

function draw() {
  if(frameCount<150) return
  frameRate(10)
  print(frameCount)
  background(220)
  dir=randomDir()
  if (dir==0) pi=(pi+1)%n
  if (dir==1) pj=(pj+1)%n
  if (dir==2) pi=(pi+n-1)%n
  if (dir==3) pj=(pj+n-1)%n
//  if ((pi+pj)%2==0) listCell[pi][pj]=true
//  else listCell[pi][pj]=false
  listCell[pi][pj]=randomBool()
  for(i=0;i<n;i+=1){
    for(j=0;j<n;j+=1){
      if (listCell[i][j]) drawCellA(i,j)
      else drawCellB(i,j)
    }
  }
  push()
  fill("black")
  translate(pi*cellSize,pj*cellSize)
  rect(cs2,cs2,cs2,cs2)
  pop()
}

function drawCellA(i,j){
  push()
  noStroke()
  translate(i*cellSize,j*cellSize)
  var col1=vcol1
  var col2=vcol2
  if ((i+j)%2==1) {
    col1=vcol2
    col2=vcol1
  }
  fill(col1)
  rect(0,0,cellSize,cellSize)
  fill(col2)
  rect(0,0,cs2,cs2)
  rect(cs2,cs2,cs2,cs2)
  fill(col1)
  rect(cs4,cs4,cs2,cs2)
 // arc(0,0,cellSize,cellSize,0,90)
 // arc(cellSize,cellSize,cellSize,cellSize,180,270)
  pop()
}

function drawCellB(i,j){
  push()
  noStroke()
  translate(i*cellSize,j*cellSize)
  var col1=vcol1
  var col2=vcol2
  if ((i+j)%2==0) {
    col1=vcol2
    col2=vcol1
  }
  fill(col1)
  rect(0,0,cellSize,cellSize)
  fill(col2)
  rect(cs2,0,cs2,cs2)
  rect(0,cs2,cs2,cs2)
  fill(col1)
  rect(cs4,cs4,cs2,cs2)
//  arc(cellSize,0,cellSize,cellSize,90,180)
//  arc(0,cellSize,cellSize,cellSize,270,360)
  pop()
}