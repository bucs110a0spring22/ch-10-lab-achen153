import pygame
import random
from src import utility
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
        w, h = pygame.display.get_window_size()
        self.rect.x = self.rect.x + random.choice((-1,0,1))
        self.rect.y = self.rect.y + random.choice((-1,0,1))
        #print("'Update me,' says " + self.name)
        if self.rect.y > utility.Utility.screen_height - 90:
            self.rect.y -= 1
        elif self.rect.y < 0:
            self.rect.y += 1
        if self.rect.x > utility.Utility.screen_width - 120:
            self.rect.x -= 1
        elif self.rect.x < 0:
            self.rect.x += 1 


#width=640, height=480