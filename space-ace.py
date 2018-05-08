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
    
    def game_over(self):
        # Clear previous surface
        self.asteroid_sprites.clear(self.screen, self.background)
        self.asteroid_sprites.empty()
        # Load text font and images
        self.font_gameover = load_fonts('Game Over', 95, (42, 247, 44))
        self.font_final_score = load_fonts('Score: %d' %self.score 50, (255, 255, 255))
        self.enter_initials = load_fonts('Enter initials: ', 50, 2(55, 255, 255))
    
    def load_character_selection(self):
        # Clear previous surface
        self.screen.fill((0,0,0))
        self.star_sprites.clear(self.screen, self.background)
        self.asteroid_sprites.empty()
        # Load text font and images
        font_choose_pilot = load_fonts('Choose your pilot: ', 50, (255, 255, 255))
        text_name_junior = load_fonts('Name: Junior', 30, (255, 255, 255))
        text_name_reggie = load_fonts('Name: Reggie', 30, (255, 255, 255))
        text_name_eve = load_fonts('Name: Eve', 30, (255,255,255))
        text_lives = load_fonts('Lives: 9', 30, (255, 255, 255))
        text_ship = load_fonts('Ship: ', 30, (255, 255, 255))

        # Add text to screen
        self.screen.blit(font_choose_pilot, [25, 25])
        self.screen.blit(text_name_junior, [95, 470])
        self.screen.blit(text_name_reggie, [525, 470])
        self.screen.blit(text_name_eve, [955, 470])
        self.screen.blit(text_lives, [95, 530])
        self.screen.blit(text_lives, [525, 530])
        self.screen.blit(text_lives, [955, 530])
        self.screen.blit(text_ship, [95, 530])
        self.screen.blit(text_ship, [525, 580])
        self.screen.blit(text_ship, [955, 580])
        # Create Static_Image objects
        static_image_group = pygame.sprite.Group(Static_Image('assets/tbd.png', (105, 175, 144, 119)),
                                                 Static_Image('assets/Cat2.png', (535, 175, 144, 119)),
                                                 Static_Image('assets/Cat3.png', (965, 175, 144, 119)),
                                                 Static_Image('assets/button_inactive.png', (150, 700, 250, 68)),
                                                 Static_Image('assets/button_inactive.png', (580, 700, 250, 68)),
                                                 Static_Image('assets/button_inactive.png', (1010, 700, 250, 68)),
                                                 Static_Image('assets/Ship1.png', (285, 580, 75, 73)),
                                                 Static_Image('assets/Ship2.png', (710, 580, 75, 73)),
                                                 Static_Image('assets/Ship3.png', (1135, 580, 75, 73))
                                                )

        # Draw static_image_group to screen
        static_image_group.draw(self.screen)
        pygame.display.update()
    
    def stage_one(self, reset):
        if reset:
            if self.lives == 0:
                self.level = "game_over"
                self.game_over()
            else:
                self.screen.blit(self.font_score, [1180, 870])
                self.ship_sprites = self.load_ship_sprite(self.character)
                self.ship_sprites.draw(self.screen)
                self.asteroid_sprites.empty()
                self.stage_time = time.time()
        else:
            # Clear previous surface
            self.screen.fill((0,0,0,))
            self.star_sprites.clear(self.screen, self.background)
            self.star_sprites.empty()
            # Reset game variables
            self.stage_time = time.time()
            self.screen.blit(self.health_bar_surface, [844, 215])
            self.ship_sprites = self.load_ship_sprite(self.character)
            self.ship_sprites.draw(self.screen)
            self.asteroid_sprites = pygame.sprite.Group()
            pygame.display.update()    
    
    def load_ship_sprite(self, character):
        # Create and assign new Ship objectt to sprite group
        self.ship = Ship(character)
        self.ship_sprites = pygame.sprite.Group(self.ship)
        return self.ship_sprites
    
    def load_intro(self):

    def update_star_sprites(self):
        colors = [(0, 0, 255), (255, 255, 255), (255, 0, 0)]
        numHorizontal = int(self.width / 50)
        numVertical = int(self.height / 50)
        self.star_sprites = pygame.sprite.Group()
        time.sleep(0.75)

        for i in range(numHorizontal * 2):
            x = random.randint(0, numHorizontal) * 50
            y = random.randint(0, numVertical) * 50
            if x not in range(290, 1135) or y not in range(145, 420):
                self.star_sprites.add(Stars(pygame.Rect(x, y, 50, 50), random.choice(colors)))
    
        
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