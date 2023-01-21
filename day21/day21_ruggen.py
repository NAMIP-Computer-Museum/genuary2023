"""
Genuary2022 Day 21 - Rug Generator by C. Ponsard
Free under the terms of GPLv3 license

see https://books.google.be/books?id=NuFeW8N2hlkC&pg=PA340&lpg=PA340&dq=oriental+rug+simple+algo
"""

import os, sys, random
import pygame
from pygame.locals import *
from pygame import Color as col

import numpy as np

# Constants
SCREEN_W, SCREEN_H = (800, 600)
# N = 129
COL= [ col("darkred"), col("firebrick"), col("crimson"),col("firebrick4"),col("brown"),col("yellow"),col("red3"), col("gold"),
       col("red"), col("chocolate4"), col("white"),col("orange"),col("orangered"),col("red"),col("sienna"), col("tomato3") ]

def colorSquare(art,x,y,w,h,shift):
    if (w<=2) and (h<=2): return

    tlc=art[x,y]
    trc=art[x+w-1,y];
    blc=art[x,y+h-1];
    brc=art[x+w-1,y+h-1];
    ncol = (int((tlc+trc+blc+brc)/4)+shift)%16;
#  print(x,y,x+w-1,y+h-1,"C:",tlc,trc,blc,brc,ncol);
    w2=int(w/2);
    h2=int(h/2);
#    print("W: ",str(w2));
    xc=x+w2;
    yc=y+h2;
    art[xc,y+1:y+h-1] = ncol;
    art[x+1:x+w-1,yc] = ncol;

    colorSquare(art,x,y,w2+1,h2+1,shift);
    colorSquare(art,xc,y,w2+1,h2+1,shift);
    colorSquare(art,x,yc,w2+1,h2+1,shift);
    colorSquare(art,xc,yc,w2+1,h2+1,shift);

def colorRug(art, n, initCol, shift):
    #border
    art[:,0] = initCol
    art[:, n-1] = initCol
    art[0, :] = initCol
    art[n-1, :] = initCol

    # start recursion
    colorSquare(art,0,0,n,n,shift)

def main():
    # basic start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Genuary2023 - DAY21 - Rug Generator by C.Ponsard')

    clock = pygame.time.Clock()
    n = 3
    d = 1
    while 1:
        clock.tick(2/(n-1))

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

        N = 2**n+1;

        img = pygame.Surface((N, N))
        art = np.zeros((N, N), dtype=int)
        #    print(art.shape)

        # test pattern
        # for x in range(N):
        #    art[x].fill(int(x / N * 255))

        colorRug(art, N, 6, 13)
        #print(art)
        #    art = art*16
        rgb = np.zeros((N, N, 3), dtype=int)
        #    rgb = np.repeat(art[:, :, np.newaxis], 3, axis=2)
        #    print(rgb.shape)
        #    print(rgb[:, :, 0])
        for x in range(N):
            for y in range(N):
                rgb[x, y, 0] = COL[art[x, y]].r
                rgb[x, y, 1] = COL[art[x, y]].g
                rgb[x, y, 2] = COL[art[x, y]].b

        pygame.surfarray.blit_array(img, rgb)
        disp = pygame.transform.scale(img,(SCREEN_W,SCREEN_H))
        screen.blit(disp, (0, 0))

        n=n+d
        if (n==3) or (n==9): d=-d

        pygame.display.flip()

if __name__ == '__main__': main()