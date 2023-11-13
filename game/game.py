import pygame
import random
import sys

from game_parameters import *
from background import draw_background
from lumberjack import Lumberjack

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#add clock
clock = pygame.time.Clock()

#Main Loop
running = True
background = screen.copy()
draw_background(background)

#spawn lumberjack
lumberjack = Lumberjack(SCREEN_WIDTH/2, SCREEN_HEIGHT- 1.8*TILE_SIZE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #controls the player with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lumberjack.move_left()
            if event.key == pygame.K_RIGHT:
                lumberjack.move_right()

        #stops player when key is lifted
        if event.type == pygame.KEYUP:
            lumberjack.stop()

    #draw background:
    screen.blit(background, (0,0))

    lumberjack.update()

    lumberjack.draw(screen)

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()