"""
Genuary2022 Day 1 - Perfect Loop by C. Ponsard
Free under the terms of GPLv3 license
"""

import os, sys, random
import pygame
from pygame.locals import *

# Constants
SCREEN_W, SCREEN_H = (600, 600)
RW = 10
SW = 76
SPEED = 15
P1 = 22
P2 = 622
NINV = 30
RECORD = False
hunt = False
pause = False
over = False

class MySprite():

    def __init__(self, name, n, px0, py0):
        self.name = name
        self.n = n
        self.img = []
        if n>1:
            self.z = 1
            for i in range(n):
                filename = '../day1/day1_img/'+name+str(i+1)+'.png'
                loaded = pygame.transform.flip(pygame.image.load(filename).convert_alpha(), True, False)
                self.img.append(pygame.transform.rotozoom(loaded,0.0, self.z))
        else:
            self.z = 0.3
            filename = '../day1/day1_img/' + name + '.png'
            loaded = pygame.image.load(filename).convert_alpha()
            self.img.append(pygame.transform.rotozoom(loaded, 0.0, self.z))

        self.px = px0
        self.py = py0
        self.dx = SPEED
        self.dy = 0
        self.ind = 0
        if n==4:
            self.dir = 2
            self.ind = 2
            self.dx = -self.dx
        else:
            self.dir = 0
        print("init "+self.name+str(self.img[0]))

    def isPacman(self):
        return self.n > 1

    def draw(self, screen):
        global hunt
        cimg = self.img[self.ind]
        if hunt and not self.isPacman(): cimg = afraid

        if self.dx>0 :
            screen.blit(cimg, (int(self.px), int(self.py)))
        else:
            if self.isPacman() and (self.dy != 0):
                if self.dy>0:
                    rot=-90
                else:
                    rot=90
                timg=pygame.transform.rotozoom(cimg, rot, 1.0)
                screen.blit(timg, (int(self.px), int(self.py)))
            else:
                screen.blit(pygame.transform.flip(cimg, True, False), (int(self.px), int(self.py)))

        color = (0, 0, 0)
        global mask
        pygame.draw.rect(mask, color, pygame.Rect(int(self.px),int(self.py),SW,SW))

    def update(self):
        global over
        if over: return

        self.ind = int((self.px+self.py)/20) % self.n     # index
        self.px = self.px+self.dx
        self.py = self.py+self.dy

#        print(self.dir)
        global hunt
        d=1
        if hunt: d=-1
        step = int(self.dir/4)

    #    if (self.dir%4==0) and self.px<SW*step: step=step-1 # correctif

    #    if self.isPacman(): print("DIR: ",self.dir%4," STEP: ",step," POS: ",self.px," ",self.py)
        if (self.px<SW*step):              # a gauche
    #        print("a gauche ",self.px," ",SW*step)
            if self.dx < 0:
                self.dir = (self.dir+d)
                self.px=SW*step
        elif (self.px>SCREEN_W-SW*(step+1)): # a droite
    #        print("a droite",self.px," ",SCREEN_W-SW*(step+1))
            if self.dx > 0:
                self.dir = (self.dir+d)
                self.px=SCREEN_W-SW*(step+1)
        elif (self.py<SW*(step+1)):              # en haut
    #        print("en haut",self.py," ",SW*(step+1))
            if self.dy < 0:
                self.dir = (self.dir+d)
                self.py=SW*(step+1)
        elif (self.py>SCREEN_H-SW*(step+2)): # en bas
    #        print("en bas",self.py,' ',SCREEN_H-SW*(step+2))
            if self.dy > 0:
                self.dir = (self.dir+d)
                self.py=SCREEN_H-SW*(step+2)

        #if (self.dir == 2) and (self.dx < 0) and (self.px < P1) and self.isPacman(): hunt = True
        #if (self.dir == 0) and (self.dx < 0) and (self.px < P2) and self.isPacman(): hunt = False

        speed = SPEED
        if hunt:
            if self.isPacman(): speed = SPEED
            else: speed = 0.95*SPEED
        else:
            if self.isPacman(): speed=0.95*SPEED
            else: speed = SPEED

        if self.dir%4 == 0:  # bas
            self.dx = speed
            self.dy = 0
  #          self.py = SCREEN_H-RW-SW*(step+1)
        elif self.dir%4 == 1:  # droite
            self.dx = 0
            self.dy = -speed
  #          self.px = SCREEN_W-RW-SW*(step+1)
        elif self.dir%4 == 2: # haut
            self.dx = -speed
            self.dy = 0
  #          self.py = RW+SW*step
        else:                 # gauche
            self.dx = 0
            self.dy = speed
  #          self.px = RW+SW*step
        if hunt:
            self.dx = -self.dx
            self.dy = -self.dy



#    def in_screen(self):
#        if self.px<-0: return False
#        if self.py<-0: return False
#        if self.px>SCREEN_W-self.img.get_width(): return False
#        if self.py>SCREEN_H-self.img.get_height(): return False
#        return True

def main():
    # basic start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Genuary2023 - DAY31 - Deliberately break by C.Ponsard')
    global afraid
    img = pygame.image.load('../day1/day1_img/afraid.png').convert_alpha()
    afraid = pygame.transform.rotozoom(img, 0.0, 0.3)

    invaders = []
    for i in range(NINV):
        fname = "img/invaders-"+str(i+1)+".png"
        tmp = pygame.image.load(fname).convert_alpha()
        tmp = pygame.transform.scale(tmp, (SCREEN_W,SCREEN_H))
        invaders.append(tmp)

    # create background
    global mask
    mask = pygame.Surface(screen.get_size(),pygame.SRCALPHA, 32)

    # create sprites
    sprites = []
    sprites.append(MySprite("blinky",1,10,SCREEN_H-SW))
    sprites.append(MySprite("clyde",1,110,SCREEN_H-SW))
    sprites.append(MySprite("inky",1,210,SCREEN_H-SW))
    sprites.append(MySprite("pinky",1,310,SCREEN_H-SW))
    sprites.append(MySprite("pacman",4,SCREEN_W-1-SW,0))

    #list=pygame.font.get_fonts()
    #for i in range(len(list)):
    #    print(list[i])

    font = pygame.font.SysFont("smallpixel7", 100) # need to install font !

    clock = pygame.time.Clock()
    n=1000
    global hunt
    global over

    while 1:
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                global pause
                pause = not pause

        num = int(n/10)%NINV-10
        #print(num)
        screen.blit(invaders[num], (0, 0))
        screen.blit(mask, (0, 0))

        if n>1030:
            for i in range(len(sprites)):
                sprites[i].draw(screen)
                if not(pause) and (n>1050): sprites[i].update()

        if over:
            text = font.render("Genuary Over", False, (230, 0, 230))
            screen.blit(text, (100, SCREEN_H/2-200))
            text = font.render("Ready Player 1", False, (50, 255, 50))
            screen.blit(text, (50, SCREEN_H/2+140))

        if RECORD and n<2000: pygame.image.save(screen,'TEMP/day1_'+str(n)+'.png')
        n = n+1

        #if n==1208: hunt=True
        #if n==1234: over=True
        if n==1208: hunt=True
        if n==1300: hunt=False
        if n==1465:
            over=True
            sprites[4].dx=-SPEED
            sprites[4].dy=0

        pygame.display.flip()


if __name__ == '__main__': main()