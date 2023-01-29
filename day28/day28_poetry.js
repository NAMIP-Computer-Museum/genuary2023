let lexicon;
let json;
let grammar;
let words=[];
let prev="";

//   "7plus5": "(I wake and look for water % $vp5) | ($12sen $tree) | (I $myad $myact $myobj % $vp5)",

function preload() {
  json = loadJSON('haiku.json');
}

function setup() {
  grammar = RiTa.grammar(json);
  createCanvas(800, 400);
  textSize(55);
  textStyle(BOLD);
//  text("Click for phrase", width/2, height/2);

  colorMode(HSB,255);
  frameRate(25);
}

function draw() {
  background("beige");
  let pg=frameCount%150;
  if (pg==1) {
    newHaiku()
    for (let word of words) word.spread()
  }
//  if (frameCount%100==75) {
//    for (let word of words) word.reset()
//  }

  for (let i = 0; i < words.length; i++) {
    const word = words[i] // retrieve word object
    if (pg>70) word.update()
    word.display()
  }
}

function newHaiku() {
  while(true) {
    str = grammar.expand()
    wordsStr = str.split(' ')
    if (wordsStr[1]!=prev) break
  }
  prev = wordsStr[1]
  words = [];

  // track word position
  let x = 60
  let y = 100
  fill(255)
  // iterate over each word
  for (let i = 0; i < wordsStr.length; i++) {
    const wordStr = wordsStr[i] // get current word
    if ((wordStr=="%") || (x > width)) {
      y += 80 // line height, sort of
      x = 60 // reset x position
      continue
    }

    const wordStrWidth = textWidth(wordStr) // get current word width
    const word = new Word(wordStr, x, y, i)
    words.push(word)
    x = x + wordStrWidth + textWidth(' ') // update x by word width + space character
    // look ahead the next word - will it fit in the space? if not, line break
  }
}

function gen1OLD() {
  let output =
  "The " +
  RiTa.randomWord({pos: "nn"}) +
  " " +
  RiTa.randomWord({pos: "vbd"}) +
  " with the " +
  RiTa.randomWord({pos: "jj"}) +
  " " +
  RiTa.randomWord({pos: "nn"}) +
  ".";
  return [ output ];
}

function gen2OLD() {
  let result = grammar.expand();
  let haiku = result.split("%");
  return haiku;
}

function gogenOLD() {
  background(50);
  textAlign(LEFT, TOP);
  let gt=gen2();
  print(gt.length)
  for(let i=0; i<gt.length; i++) {
    print(i,gt[i]);
    text(trim(gt[i]), 10, 10+i*30, width-20, height-20);
  }
}


class Word {
            constructor(word, x, y, idx) {
                this.word = word
                this.x = x
                this.y = y
                this.color = color(255)
                // target position is the same as current position at start
                this.tx = this.x
                this.ty = this.y
                this.tcolor = this.color;
                // original position
                this.origx = this.x
                this.origy = this.y
                this.idx = idx
            }

            reset() {
                this.tx = this.origx
                this.ty = this.origy
                this.color = color(255)
            }

            spread() {
                this.x = random(width-200)
                this.y = 40+random(height-50)
                this.color = color(random(255),200,240)
            }

            update() {
                // move towards the target by 10% each time
                this.x = lerp(this.x, this.tx, 0.09)
                this.y = lerp(this.y, this.ty, 0.09)
//                this.color =  color(lerp(this.color[0],this.tcolor[0],0.1),
//                                    lerp(this.color[1],this.tcolor[1],0.1),
//                                    lerp(this.color[2],this.tcolor[2],0.1))
            }

            display() {
                fill(this.color)
                noStroke()
//                stroke("black")
//                strokeWeight(4)
                text(this.word, this.x, this.y)
            }
}