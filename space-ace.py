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

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image_file, x_axis):
        # Call parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_file)
        self.rect = Rect(x_axis, 0, 35, 32)
    
    def move(self, screen_rect):
        self.rect.move_ip(0,10)

class Stars(pygame.sprite.Sprite):
    pygame.sprite.Sprite.__init_(self)
    self.image = pygame.Surface((3,3))
    self.image = self.image.convert()
    self.image.fill(color)
    self.rect = rect  
    
if __name__ == '__main__':
    main()