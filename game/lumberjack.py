import pygame
from game_parameters import *

class Lumberjack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.forward_image = pygame.image.load('../assets/sprites/lum.png')
        self.image = self.forward_image
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def jump(self):
        #placeholder for jump function



    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)
