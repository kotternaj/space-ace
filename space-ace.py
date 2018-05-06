import os, sys, random, time, string, pickle
import pygame
from pygame.locals import *
pygame.font.init()

def load_image(file_name):
    image = pygame.image.load(file_name)
    image = image.convert()
    return image

def load_fonts(text, size, color):
    font = pygame.font.Font('freesansbold.tff, size')
    space_font = font.render(text, 1, color)
    return space_font

class Ship(pygame.sprite.Sprite):
    def __init__(self, character):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(character)
        self.rect = self.image.get_rect()
        self.rect.top = 770
        self.rect.left = 685
        self.x_dist = 50
        self.y_dist = 50
        self.is_alive = True
    
    def move(self, key, screen_rect):
        xMove = 0
        yMove = 0
        if (key == pygame.K_RIGHT):
            xMove = self.x_dist
        elif (key == pygame.K_LEFT):
            xMove = -self.x_dist
        elif (key == pygame.K_DOWN):
            yMove = self.y_dist
        elif (key == pygame.K_UP):
            yMove = -self.y_dist
        self.rect.move_ip(xMove, yMove)
        self.rect.clamp_ip(screen_rect)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image_file, x_axis):
        # Call parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_file)
        self.rect = Rect(x_axis, 0, 35, 32)
    
    def move(self, screen_rect):
        self.rect.move_ip(0,10)

class Stars(pygame.sprite.Sprite):
    def __init__(self, rect, color):
        pygame.sprite.Sprite.__init_(self)
        self.image = pygame.Surface((3,3))
        self.image = self.image.convert()
        self.image.fill(color)
        self.rect = rect  

class Static_Image(pygame.sprite.Sprite):
    def __init__(self, file_name, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(file_name)
        self.rect = pygame.Rect(rect)

if __name__ == '__main__':
    main()