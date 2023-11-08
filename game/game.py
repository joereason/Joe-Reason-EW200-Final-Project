import pygame
import random
import sys

from game_parameters import *
from background import draw_background

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw background:
    screen.blit(background, (0,0))

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()