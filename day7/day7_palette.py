"""
Genuary2022 Day 7 - Sample a Palette C. Ponsard
Free under the terms of GPLv3 license
"""
import gc
import os, sys, random
import pygame
from pygame.locals import *
import colorsys
import math

# Constants
SCREEN_W, SCREEN_H = (460, 700)

MS = 10
MP = 8
MM = 10
MT = 13
MAX = MS*2+MP*2+MM+MT

def touch(tab,i):
    col = tab[i]
    hsv = colorsys.rgb_to_hsv(col.r/255, col.g/255, col.b/255)
    rgb = colorsys.hsv_to_rgb(hsv[0], 1.0, hsv[2])
#    tab[i].r = int(rgb[0]*255)
#    tab[i].g = int(rgb[1]*255)
#    tab[i].b = int(rgb[2]*255)

def getColorValue_old(tab,i):
#    hsva = pygame.Color(col).hsva
    col = tab[i]
    r = int(col.r/16)*16
    g = int(col.g/16)*16
    b = int(col.b/16)*16
    hsv = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    h = hsv[0] + 0.15
    if h > 1.0: h = h - 1.0

    rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
    tab[i].r = int(rgb[0]*255)
    tab[i].g = int(rgb[1]*255)
    tab[i].b = int(rgb[2]*255)

    return h
#    return col.r+col.g+col.b

def getColorValue(col):
    repetitions = 10
    r = col.r/255
    g = col.g/255
    b = col.b/255
    lum = math.sqrt(.241 * r + .691 * g + .068 * b)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    hc = h + 0.08
    if hc > 1.0: hc = hc - 1.0
    h2 = int(hc * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)
    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum

    return (h2, lum, v2)

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):

    touch(array,j)
    if getColorValue(array[j]) <= getColorValue(pivot):
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
    touch(array,pi)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

# Python program for implementation of Bubble Sort
def bubbleSort(arr,max):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        if i>max: return
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if getColorValue(arr,j) > getColorValue(arr,j+1):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def sort(img,step):
    tab = []
    w, h = img.get_size()
    for y in range(h):
        for x in range(w):
            tab.append(img.get_at((x,y)))
    print(tab)
    bubbleSort(tab,step*10)

    tab2 = []
    for i in range(len(tab)):
        tab2.append(getColorValue(tab,i))
    print(tab2)

    i = 0
    for y in range(h):
        for x in range(w):
            img.set_at((x,y),tab[i])
            i = i+1

def sort_lines(img,l):
    w, h = img.get_size()
    if l>h: l = h
    for y in range(l):
        tab = []
        for x in range(w):
            tab.append(img.get_at((x, y)))
        quickSort(tab,0,w-1)
        for x in range(w):
            img.set_at((x,y),tab[x])

def forward(img,step):
    if step == 1: return img

    if step<MS:
#        n = 2**(step-1)
        n = 2*step
        print(n)
        low = resample(img,n)
        return pygame.transform.scale(low,(SCREEN_W,SCREEN_H))

    low = resample(img, 2*MS)
    print("HEIGHT: "+str(low.get_height()))
    step = step-MS
    if step>MP: step = MP
    sort_lines(low,step*5)
    return pygame.transform.scale(low,(SCREEN_W,SCREEN_H))

def compute(img,step):
    print("STEP: "+str(step))
    if step<MS+MP:
        return forward(img,MS+MP-step)
    if step<=MS+MP+MM:
        return img
    return forward(img,step-MS-MP-MM)

def resample(img,n):
    w = int(img.get_width()/n)
    h = int(img.get_height()/n)
    return pygame.transform.scale(img,(w,h))

def main():
    # basic start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Genuary2023 - DAY7 - Color Palette by C.Ponsard')
    poster01 = pygame.image.load('BFP01.jpg')
    poster02 = pygame.image.load('BFP02.jpg')
    poster03 = pygame.image.load('BFP03.jpg')
    poster = [poster01, poster02, poster03]

    clock = pygame.time.Clock()
    np = 0
    step = 1
    pause = False

    while 1:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                pause = not pause

        pygame.display.flip()
        if step<MAX-MT:
            img = compute(poster[np],step)
            screen.blit(img, (0, 0))
        else:
            dec=step-MAX+MT
            print("ICI "+str(dec))
            img1 = compute(poster[np],1)
            img2 = compute(poster[(np+1)%3],1)
            screen.blit(img1, (0, 0))
            screen.blit(img2, (0, 0),(0, 0, img2.get_width(), dec*20*3))

        if not pause: step = step + 1
        if (step == MAX):
            step = 1
            np = (np+1)%3

if __name__ == '__main__': main()