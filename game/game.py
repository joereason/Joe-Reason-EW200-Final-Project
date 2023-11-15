import pygame
import random
import sys

from game_parameters import *
from background import draw_background, add_deer
from lumberjack import Lumberjack
from deer import deer

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

add_deer(2)

#spawn lumberjack
lumberjack = Lumberjack(SCREEN_WIDTH/2, SCREEN_HEIGHT- 2.2*TILE_SIZE)

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
            if event.key == pygame.K_UP:
                lumberjack.jump()

        #stops player when key is lifted
        if event.type == pygame.KEYUP:
            lumberjack.stop()

    #define boarders at edge of screen
    if lumberjack.x > SCREEN_WIDTH-30:
        lumberjack.x = SCREEN_WIDTH-30
    if lumberjack.x < -15:
        lumberjack.x = -15
    if lumberjack.y > SCREEN_HEIGHT - 2.2*TILE_SIZE:
        lumberjack.y = SCREEN_HEIGHT - 2.2*TILE_SIZE

    #draw background:
    screen.blit(background, (0,0))

    deer.update()
    lumberjack.update()

    for d in deer:
        if d.rect.x < -d.rect.width:  # use the tile size
            deer.remove(d)  # remove the fish from the sprite group
            add_deer(1)

    #draw the game objects
    deer.draw(screen)
    lumberjack.draw(screen)

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()