import pygame
import random
from game_parameters import *
import math

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/sprites/zombie.png').convert()
        self.forward_image = pygame.image.load('../assets/sprites/zombie.png').convert()
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.image.set_colorkey((255, 255, 255))
        self.forward_image.set_colorkey((255, 255, 255))
        self.reverse_image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 0.7
        self.rect.center = (x, y)
        self.player = player

    #makes zombie follow the player named 'object'
    def update(self):
        self.rect.x = self.x
        if self.x < self.player.x:
            self.x += self.speed
        elif self.x > self.player.x:
            self.x -= self.speed

    def draw(self, surf):
        surf.blit(self.image, self.rect)

zombies = pygame.sprite.Group()