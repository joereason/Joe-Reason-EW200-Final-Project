import pygame
import random
import sys

from game_parameters import *
from background import draw_background, add_deer, add_wood
from lumberjack import Lumberjack
from robber import Robber
from deer import deer
from wood import wood
from raven import Raven

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

#initialize final screen font
final_score_font = pygame.font.Font('../assets/fonts/scoreboard.ttf', 30)

lumlives = NUM_LIVES1
roblives = NUM_LIVES2

#spawn lumberjack
lumberjack = Lumberjack(SCREEN_WIDTH/2+20, SCREEN_HEIGHT- 2.2*TILE_SIZE)
robber = Robber(SCREEN_WIDTH/2-20, SCREEN_HEIGHT- 2.2*TILE_SIZE)
raven = Raven(SCREEN_WIDTH/2, 100)

#while running:
while lumlives > 0 and roblives > 0:
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
                lumberjack.isjumping = True

            #control player 2
            if event.key == pygame.K_a:
                robber.move_left()
            if event.key == pygame.K_d:
                robber.move_right()
            if event.key == pygame.K_w:
                robber.isjumping = True

        #stops player when key is lifted
        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            #prevents issue where both players stop when a key is lifted
            if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w]:
                lumberjack.stop()
            elif keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP]:
                robber.stop()
            else:
                lumberjack.stop()
                robber.stop()

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

    lumberjack.jump()
    robber.jump()
    deer.update()
    wood.update()
    lumberjack.update()
    robber.update()
    raven.hover()

    #change to hurt image when at 1 life left
    if lumlives <= 1:
        lumberjack.forward_image = pygame.image.load('../assets/sprites/hurtlum.png')
        lumberjack.reverse_image = pygame.transform.flip(lumberjack.forward_image, True, False)

    if roblives <= 1:
        robber.forward_image = pygame.image.load('../assets/sprites/hurtrobber.png')
        robber.reverse_image = pygame.transform.flip(robber.forward_image, True, False)

    #check for collisions
    lumdeercollide = pygame.sprite.spritecollide(lumberjack, deer, True)
    if lumdeercollide:
        lumlives -= len(lumdeercollide)
        add_deer(len(lumdeercollide))

    robdeercollide = pygame.sprite.spritecollide(robber, deer, True)
    if robdeercollide:
        roblives -= len(robdeercollide)
        add_deer(len(robdeercollide))

    #increase score
    lumwoodcollide = pygame.sprite.spritecollide(lumberjack, wood, True)
    if lumwoodcollide:
        #this is where I add sounds
        lumscore += len(lumwoodcollide)
        add_wood(1)

    robwoodcollide = pygame.sprite.spritecollide(robber, wood, True)
    if robwoodcollide:
        # this is where I add sounds
        robscore += len(robwoodcollide)
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
    raven.draw(screen)

    #draw the score on the screen
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

#create new background when game over
screen.blit(background, (0, 0))

#show game over message
message = score_font.render('GAME OVER', True, (0, 0, 0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2-20))

#show final score
finalscore1 = final_score_font.render(f'Player 1 Score: {robscore}', True, (0, 0, 0))
finalscore2 = final_score_font.render(f'Player 2 Score: {lumscore}', True, (0, 0, 0))
screen.blit(finalscore1, (SCREEN_WIDTH / 4 - finalscore1.get_width() / 2, SCREEN_HEIGHT / 2 + finalscore1.get_height()))
screen.blit(finalscore2, (SCREEN_WIDTH*3 / 4 - finalscore2.get_width() / 2, SCREEN_HEIGHT / 2 + finalscore2.get_height()))


#update display
pygame.display.flip()

#wait for user to exit the game
while True:
    #This is where you would add 'play again' or add other levels
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Quit pygame
            pygame.quit()
            sys.exit()

#pygame.quit()
#sys.exit()