import pygame
from game_parameters import *
import random

def draw_background(surf):
    #load sprites for background
    grass = pygame.image.load('../assets/sprites/grass.png').convert()
    dirt = pygame.image.load('../assets/sprites/dirt.png').convert()
    cloud = pygame.image.load('../assets/sprites/cloud.png').convert()
    sky = pygame.image.load('../assets/sprites/sky.png').convert()
    #set colorkeys
    grass.set_colorkey((0,0,0))
    dirt.set_colorkey((0,0,0))
    cloud.set_colorkey((0,0,0))
    sky.set_colorkey((0,0,0))

    #fill screen
    skyandclouds = [cloud, sky]
    for x in range(0, SCREEN_WIDTH, 10):
        for y in range(0, SCREEN_HEIGHT, 10):
            #randomize sky and cloud textures
            num = random.randint(0,1)
            surf.blit(skyandclouds[num], (x,y))

    #draw the ground
    for x in range(0, SCREEN_WIDTH, 10):
        surf.blit(grass, (x, SCREEN_HEIGHT-2*TILE_SIZE))

    for x in range(0, SCREEN_WIDTH, 10):
        surf.blit(dirt, (x, SCREEN_HEIGHT-TILE_SIZE))

    #draw text
    custom_font = pygame.font.Font("../assets/fonts/font.ttf", 48)
    text = custom_font.render("Coin Capture", True, (255, 0, 0))
    surf.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, 0))

#placeholder for functions that add coins and other loot