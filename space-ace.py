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

class Stars(pygame.sprite.Sprite):
    pygame.sprite.Sprite.__init_(self)
    self.image = pygame.Surface((3,3))
    self.image = self.image.convert()
    self.image.fill(color)
    self.rect = rect  
    