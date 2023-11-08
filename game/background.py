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

    #draw sky
    for x in range(0, SCREEN_WIDTH, 15):
        for y in range(0, SCREEN_HEIGHT, 15):
            surf.blit(sky, (x, y))

    #draw clouds
    for x in range(0, SCREEN_WIDTH, 15):
        for y in range(70, 90, 30):
            surf.blit(cloud, (x, y))

    #draw the grass
    for x in range(0, SCREEN_WIDTH, 15):
        surf.blit(grass, (x, SCREEN_HEIGHT-1.5*TILE_SIZE))

    #draw the dirt from bottom of grass to bottom of screen
    for x in range(0, SCREEN_WIDTH, 15):
        surf.blit(dirt, (x, SCREEN_HEIGHT-1.3 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT - 1.1 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT - 0.9 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT - 0.7 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT - 0.5 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT - 0.3 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT - 0.1 * TILE_SIZE))
        surf.blit(dirt, (x, SCREEN_HEIGHT))

    #draw text
    custom_font = pygame.font.Font("../assets/fonts/font.ttf", 48)
    text = custom_font.render("Coin Capture", True, (0, 153, 0))
    surf.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, 0))

#placeholder for functions that add coins and other loot