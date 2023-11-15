import pygame
import random
from game_parameters import *

class Deer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/sprites/deer.png').convert()
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale_by(self.image, 0.4)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

deer = pygame.sprite.Group()