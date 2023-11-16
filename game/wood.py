import pygame
import random
from game_parameters import *

class Wood(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/sprites/wood.png').convert()
        self.image = pygame.transform.scale_by(self.image, 0.06)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 1.0
        self.rect.center = (x, y)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

wood = pygame.sprite.Group()