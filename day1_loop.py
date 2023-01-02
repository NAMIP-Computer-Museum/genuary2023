"""
Genuary2022 Day 1 - Perfect Loop by C. Ponsard
Free under the terms of GPLv3 license
"""

import os, sys, random
import pygame
from pygame.locals import *

# Constants
SCREEN_W, SCREEN_H = (800, 200)
RW = 10
SW = 76
SPEED = 10
P1 = 22
P2 = 622

hunt = False
pause = False

class MySprite():

    def __init__(self, name, n, px0):
        self.name = name
        self.n = n
        self.img = []
        if n>1:
            self.z = 1
            for i in range(n):
                filename = 'day1_img/'+name+str(i+1)+'.png'
                loaded = pygame.transform.flip(pygame.image.load(filename).convert_alpha(), True, False)
                self.img.append(pygame.transform.rotozoom(loaded,0.0, self.z))
        else:
            self.z = 0.3
            filename = 'day1_img/' + name + '.png'
            loaded = pygame.image.load(filename).convert_alpha()
            self.img.append(pygame.transform.rotozoom(loaded, 0.0, self.z))

        self.px = px0
        self.py = SW+RW
        self.dx = SPEED
        self.dy = 0
        self.ind = 0
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
            screen.blit(pygame.transform.flip(cimg, True, False), (int(self.px), int(self.py)))

    def update(self):
        self.ind = int(self.px/20) % self.n
        self.px = self.px+self.dx
        self.py = self.py+self.dy

        global hunt
        d=1
        if hunt: d=-1
        if (self.px<RW) or (self.px>SCREEN_W-SW-RW):
            if self.dx != 0: self.dir = (self.dir+d) % 4
        if (self.py<RW) or (self.py>SCREEN_H-SW-RW):
            if self.dy != 0: self.dir = (self.dir+d) % 4

        if (self.dir == 2) and (self.dx < 0) and (self.px < P1) and self.isPacman(): hunt = True
        if (self.dir == 0) and (self.dx < 0) and (self.px < P2) and self.isPacman(): hunt = False

        speed = SPEED
        if hunt:
            if self.isPacman(): speed=SPEED
            else: speed = 0.99*SPEED
        else:
            if self.isPacman(): speed=0.99*SPEED
            else: speed = SPEED

        if self.dir == 0:
            self.dx = speed
            self.dy = 0
            self.py = SCREEN_H-(SW+RW)
        elif self.dir == 1:
            self.dx = 0
            self.dy = -speed
            self.px = SCREEN_W-(SW+RW)
        elif self.dir == 2:
            self.dx = -speed
            self.dy = 0
            self.py = RW
        else:
            self.dx = 0
            self.dy = speed
            self.px = RW
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
    pygame.display.set_caption('Genuary2023 - DAY1 - Perfect Loop by C.Ponsard')
    global afraid
    img = pygame.image.load('day1_img/afraid.png').convert_alpha()
    afraid = pygame.transform.rotozoom(img, 0.0, 0.3)

    # create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # create sprites
    sprites = []
    sprites.append(MySprite("blinky",1,10))
    sprites.append(MySprite("clyde",1,110))
    sprites.append(MySprite("inky",1,210))
    sprites.append(MySprite("pinky",1,310))
    sprites.append(MySprite("pacman",4,P2))

    clock = pygame.time.Clock()
    while 1:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                global pause
                pause = not pause

        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        color = (0, 0, 100)
        pygame.draw.rect(screen, color, pygame.Rect(SW+RW, (SCREEN_H-4*RW)/2+RW, SCREEN_W-2*(RW+SW), 2*RW))
        pygame.draw.rect(screen, color, pygame.Rect(0, 0, RW, SCREEN_H))
        pygame.draw.rect(screen, color, pygame.Rect(SCREEN_W-RW, 0, RW, SCREEN_H))
        pygame.draw.rect(screen, color, pygame.Rect(0, 0, SCREEN_W, RW))
        pygame.draw.rect(screen, color, pygame.Rect(0, SCREEN_H-RW, SCREEN_W, RW))

        if not hunt:
            color = (200,200,0)
            pygame.draw.circle(screen, color, (RW+SW/2,RW+SW/2), 10)

        for i in range(len(sprites)):
            sprites[i].draw(screen)
            if not(pause): sprites[i].update()

        pygame.display.flip()


if __name__ == '__main__': main()