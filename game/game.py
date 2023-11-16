import pygame
import random
import sys

from game_parameters import *
from background import draw_background, add_deer, add_wood
from lumberjack import Lumberjack
from robber import Robber
from deer import deer
from wood import wood

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
add_wood(4)

life_icon = pygame.image.load('../assets/sprites/heart.png').convert()
life_icon = pygame.transform.scale_by(life_icon, 0.2)
life_icon.set_colorkey((0, 0, 0))

#initialize score for both characters
lumscore = 0
robscore = 0
score_font = pygame.font.Font('../assets/fonts/scoreboard.ttf', 48)

lumlives = NUM_LIVES1
roblives = NUM_LIVES2

#spawn lumberjack
lumberjack = Lumberjack(SCREEN_WIDTH/2+20, SCREEN_HEIGHT- 2.2*TILE_SIZE)
robber = Robber(SCREEN_WIDTH/2-20, SCREEN_HEIGHT- 2.2*TILE_SIZE)

while running:
#while lumlives > 0 and roblives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #controls the player with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lumberjack.move_left()
            if event.key == pygame.K_RIGHT:
                lumberjack.move_right()
            #if event.key == pygame.K_UP:
            #    lumberjack.jump()

            #control player 2
            if event.key == pygame.K_a:
                robber.move_left()
            if event.key == pygame.K_d:
                robber.move_right()

        #stops player when key is lifted
        if event.type == pygame.KEYUP:
            lumberjack.stop()
            robber.stop()
            #fix this

    #define boarders at edge of screen
    if lumberjack.x > SCREEN_WIDTH-30:
        lumberjack.x = SCREEN_WIDTH-30
    if lumberjack.x < -15:
        lumberjack.x = -15
    if lumberjack.y > SCREEN_HEIGHT - 2.2*TILE_SIZE:
        lumberjack.y = SCREEN_HEIGHT - 2.2*TILE_SIZE

    if robber.x > SCREEN_WIDTH-30:
        robber.x = SCREEN_WIDTH-30
    if robber.x < -15:
        robber.x = -15
    if robber.y > SCREEN_HEIGHT - 2.2*TILE_SIZE:
        robber.y = SCREEN_HEIGHT - 2.2*TILE_SIZE

    #draw background:
    screen.blit(background, (0,0))

    deer.update()
    wood.update()
    lumberjack.update()
    robber.update()

    #check for collisions
    lumresult = pygame.sprite.spritecollide(lumberjack, deer, True)
    if lumresult:
        lumlives -= len(lumresult)
        add_deer(len(lumresult))

    robresult = pygame.sprite.spritecollide(robber, deer, True)
    if robresult:
        roblives -= len(robresult)
        add_deer(len(robresult))

    #increase score
    points1 = pygame.sprite.spritecollide(lumberjack, wood, True)
    if points1:
        #this is where I add sounds
        lumscore += len(points1)
        add_wood(1)
    points1 = pygame.sprite.spritecollide(lumberjack, wood, True)

    points2 = pygame.sprite.spritecollide(robber, wood, True)
    if points2:
        # this is where I add sounds
        robscore += len(points2)
        add_wood(1)

    for d in deer:
        if d.rect.x < -d.rect.width:  # use the tile size
            deer.remove(d)  # remove the fish from the sprite group
            add_deer(1)

    #draw the game objects
    deer.draw(screen)
    wood.draw(screen)
    lumberjack.draw(screen)
    robber.draw(screen)

    #draw the score on the score
    text1 = score_font.render(f"{lumscore}", True, (0, 180, 100))
    text2 = score_font.render(f"{robscore}", True, (0, 180, 100))

    screen.blit(text1, (SCREEN_WIDTH-2*TILE_SIZE, 30))
    screen.blit(text2, (2*TILE_SIZE, 30))

#draw both lives
    for life in range(lumlives):
        screen.blit(life_icon, (((SCREEN_WIDTH-50)-life*TILE_SIZE), (SCREEN_HEIGHT - 1.4*TILE_SIZE)))

    for life in range(roblives):
        screen.blit(life_icon, ((life*TILE_SIZE), (SCREEN_HEIGHT - 1.4*TILE_SIZE)))

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()