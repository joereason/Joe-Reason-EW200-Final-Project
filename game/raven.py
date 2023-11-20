import pygame
import random
from game_parameters import *

class Raven(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.forward_image = pygame.image.load('../assets/sprites/idleraven.png')
        self.image = self.forward_image
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.x_speed = ENEMY_SPEED
        self.y_speed = ENEMY_SPEED
        self.rect.center = (x, y)

    def update(self):
        self.y += self.y_speed
        self.x += self.x_speed
        self.rect.y = self.y
        self.rect.x = self.x

    def hover(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.x += self.x_speed
        if self.x > SCREEN_WIDTH-70 or self.x < 50:
            self.x_speed = -1*self.x_speed
            if self.x > SCREEN_WIDTH/2:
                self.image = self.forward_image
            else:
                self.image = self.reverse_image

    def swoop(self):
        num = random.randint(1, 2)
        if num == 1:
            self.x_speed = 0.5
            while self.y <= SCREEN_WIDTH - 2.2*TILE_SIZE:
                self.y_speed += 2
        else:
            self.x_speed = -0.5
            while self.y <= SCREEN_WIDTH - 2.2*TILE_SIZE:
                self.y_speed += 2

    def fly_up(self):
        self.x_speed = 0
        while self.y > 100:
            self.y_speed -= 2

    def draw(self, surf):
        surf.blit(self.image, self.rect)