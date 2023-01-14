"""
Genuary2022 Day 14 - Aesemic C. Ponsard
Char Generator for use on CPC Locomotive Basic
Free under the terms of GPLv3 license
"""
import gc
import os, sys, random
import pygame
from pygame.locals import *
import colorsys
import math

# Constants
SCREEN_W, SCREEN_H = (400, 400)

def computeChar():
    tab = []
    for i in range(8):
        line=[]
        tab.append(line)
        for j in range(8):
            if (i>5) or (j>5):
                line.append(0)
            else:
                r = random.randint(0,3)
                if r>1: r=0
                line.append(r)
                if (i>0) and (r==1): tab[i-1][j]=1
    return tab

def printChar(c):
    for i in range(len(c)):
        print(c[i])

def displayChar(screen,c):
    cs = pygame.Surface((8,8))
    cs.fill([0,0,255])
    yellow = (0,255,255)
    for i in range(6):
        for j in range(6):
            if c[i][j]==1:cs.set_at((i,j),yellow)
    screen.blit(pygame.transform.scale(cs, (SCREEN_W, SCREEN_H)),(0,0))

def genSymbol(cn,c):
    res = "SYMBOL "+str(cn)
    for i in range(8):
        b = 0
        l = c[i]
        for j in range(8):
            k = 7-j
#            print(str(k)+" "+str(l[k])+" "+str(l[k]*(2**j)))
            b = b+l[k]*(2**j)
        res = res + ","+str(b)
#    printChar(c)
#    print(res)
    return res

def printListing(listing):
    for nl in listing.keys():
        print(str(nl)+" "+str(listing[nl]))

def generateCPC():
    N = 30
    START = 255-N+1
#    START = 206

    listing={}
    listing[10] = "REM GENUARY 14 - AESEMIC"
    listing[20] = "REM NEW CHARSET"
    listing[30] = "SYMBOL AFTER "+str(START)

    # charset
    charset=[]
    for i in range(N):
        c = computeChar()
        charset.append(c)
        listing[40+i*10]=genSymbol(START+i,c)
    listing[40]="SYMBOL "+str(START)+",0,0,0,0,0,0,0,0"

    inks=[25,24,22,21,19,18,17,8,16,15,7,6]
    for i in range(len(inks)):
        if (i<len(inks)-1):
            listing[800+i*10]="INK "+str(i+1)+","+str(inks[i])
        else:
            listing[800+i*10]="INK "+str(i+1)+","+str(inks[i])+",17"

    listing[1000] = "REM DISPLAY RANDOM CHARS"
    listing[1010] = "MODE 0:CLS:D=1"
    listing[1015] = 'INK 15,24,2:PEN 15:LOCATE 5,12:PRINT "RECEIVING..."'
    listing[1016] = "FOR I=1 TO 3000:NEXT I:CLS"
    listing[1020] = "FOR C=1 TO 20"
    listing[1030] = "IF (C MOD 7)=0 THEN D=D+4:GOTO 1090"
    listing[1040] = "FOR L=1 TO 20"
    listing[1050] = "PEN INT((L-1)/5)+D"
    listing[1060] = "A=INT("+str(START)+"+RND(1)*"+str(N)+")"
    listing[1070] = "LOCATE C,L:PRINT CHR$(A)"
    listing[1080] = "NEXT L"
    listing[1090] = "NEXT C"

    printListing(listing)

    # screen


def main():
    # basic start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Genuary2023 - DAY14 - Aesemics Generator by C.Ponsard')

    clock = pygame.time.Clock()
    pause = False

    while 1:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                generateCPC()
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                pause = not pause

        if not pause:
            c = computeChar()
            printChar(c)
            displayChar(screen,c)
            pause = True

        pygame.display.flip()

if __name__ == '__main__': main()