import pygame
import random
from game_parameters import *
import math

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/sprites/zombie.png').convert()
        self.forward_image = pygame.image.load('../assets/sprites/zombie.png').convert()
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 0.7
        self.rect.center = (x, y)

    #makes zombie follow the player named 'object'
    def update(self, object):
        self.x += self.speed
        self.rect.x = self.x
        if self.x >= object.x:
            self.x -= self.speed
            self.image = self.forward_image
        else:
            self.x += self.speed
            self.image = self.reverse_image

    def draw(self, surf):
        surf.blit(self.image, self.rect)

zombies = pygame.sprite.Group()