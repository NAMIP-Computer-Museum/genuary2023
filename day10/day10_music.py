"""
Genuary2023 Day 10 Generative music on Destroy a square
Tribute to breakout by C. Ponsard
Free under the terms of GPLv3 license

Run and press space TWICE to start
"""
import colorsys

import pygame
from pygame.locals import *
from pygame import mixer
from pygame import midi
from perlin_noise import PerlinNoise
import random

# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
BALL_DIAM = 16
BRICK_WIDTH, BRICK_HEIGHT = 32, 32
BALL_SPEED = 25
CHANNELS = 15

class Breakout_Sprite(pygame.sprite.Sprite):
    """ Breakout Sprite class that extends following classes

        Attributes:
            image_file (str): Sprite-image filename.
    """
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)

        # load image & rect
        self.image = pygame.image.load('images/' + image_file).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

class Brick(pygame.sprite.Sprite):
    """ Brick: Statically positionned in (x, y).
    """
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)

        # load image & rect
        self.image = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.color = color


class Ball(pygame.sprite.Sprite):
    """ Ball: Moves according to speed (speed_x, speed_y).

        Attributes:
            speed_x (int): Ball's x-speed.
            speed_y (int): Ball's y-speed.
    """
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([BALL_DIAM, BALL_DIAM])
        pygame.draw.circle(self.image, color, (BALL_DIAM/2, BALL_DIAM/2), BALL_DIAM/2)
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOW_HEIGHT/2 +8
        self.rect.left = WINDOW_WIDTH /2 -10
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        # bounce against borders
        if self.rect.x > WINDOW_WIDTH - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
            sounds["border"].set_volume(8)  # maybe windows will equalize
            sounds["border"].play()
        if self.rect.y > WINDOW_HEIGHT - self.image.get_height() or self.rect.y < 0:
            self.speed_y *= -1
            sounds["border"].set_volume(8)  # maybe windows will equalize
            sounds["border"].play()

def loadSounds():
    sounds = {}
    sounds["ambience"] = mixer.Sound("sounds/mixkit-game-level-music-689.wav")
    sounds["border"] = mixer.Sound("sounds/mixkit-small-hit-in-a-game-2072.wav")
    return sounds

def genNoise(noise,x,y):
    res=int((noise([x, y]) + 1) * 255)%255
    print(res)
#    if res<0: res = 0
#    if res>255: res = 255
    return res

def main():
    # game init
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Genuary2022 - DAY5 - Breakout the square  by C.Ponsard - PRESS SPACE TWICE')
    pygame.key.set_repeat(400, 30)
    clock = pygame.time.Clock()
    score = 0

    # sound init and ambience start
    mixer.init()
    mixer.set_num_channels(CHANNELS)
    global sounds
    sounds = loadSounds()
    sounds["ambience"].set_volume(2) # maybe windows will equalize
    sounds["ambience"].play(-1)

    midi.init()
    global player
    player = midi.Output(0)
    player.set_instrument(10)
#    player.note_on(50, 127)
#    time.sleep(1)
#    player.note_off(64, 127)

    # groups
    all_sprites_group = pygame.sprite.Group()
    player_bricks_group = pygame.sprite.Group()
    bricks_group = pygame.sprite.Group()

    orange = Color(255,160,55)
    red = Color(200,0,0)

    # add sprites to their group
    ball = Ball(red)
    all_sprites_group.add(ball)

    noise1 = PerlinNoise(octaves=2,seed=1)
    for i in range(17):
        for j in range(17):
            h = genNoise(noise1,i/17,j/17)
            s = 180
            v = 180
            rgb = colorsys.hsv_to_rgb(h/255,s/255,v/255)
            col = Color(int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))
            brick = Brick(col, (i+1)*(BRICK_WIDTH + 2), (j+1)*(BRICK_HEIGHT + 2))
    #        if i==9 and j==9: continue
            all_sprites_group.add(brick)
            bricks_group.add(brick)
            player_bricks_group.add(brick)

    clock = pygame.time.Clock()
    space = 0

    # game loop
    while True:
        clock.tick(10)

        # move player horizontally
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                space = space+1
                if space==2:
                    ball.speed_x=BALL_SPEED
                    ball.speed_y=BALL_SPEED

        # collision detection (ball bounce against brick & player)
        hits = pygame.sprite.spritecollide(ball, player_bricks_group, False)
        if hits:
            hit_rect = hits[0].rect
            col = hits[0].color
            # note = int((col.r+col.g+col.b)/750*127)
            hsv = colorsys.rgb_to_hsv(col.r/255,col.g/255,col.b/255)
            note = int(hsv[0]*40+50)
            print(note)

            # bounce the ball (according to side collided)
            if hit_rect.left > ball.rect.left or ball.rect.right < hit_rect.right:
                ball.speed_y *= -1
                player.note_on(note, 127)
            else:
                ball.speed_x *= -1
                player.note_on(note, 127)

            # collision with blocks
            if pygame.sprite.spritecollide(ball, bricks_group, True):
                score += len(hits)
                print("Score: %s" % score)

        # render groups
        window.fill((0, 0, 0))
        all_sprites_group.draw(window)

        if space<1:
            pygame.draw.rect(window, orange,(BRICK_WIDTH+2,BRICK_HEIGHT+2,WINDOW_WIDTH-2*BRICK_WIDTH,WINDOW_HEIGHT-2*BRICK_HEIGHT))

        # refresh screen
        all_sprites_group.update()
        clock.tick(60)
        pygame.display.flip()

if __name__ == '__main__': main()