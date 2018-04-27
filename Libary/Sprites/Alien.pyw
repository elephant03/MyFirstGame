import pygame
import random

# Imports the alien's laser sprite file
# Written out by editing the path as it is more relable then pythons cross file imports
import os
import sys
filename = "Libary/Sprites/AlienLaser.pyw"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    AlienLaser = __import__(module_name)
finally:
    sys.path[:] = path  # restore

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Alien(pygame.sprite.Sprite):
    '''This class repersents the aliens on screen'''

    def __init__(self):
        '''Creats the alien body and applys its graphics'''
        super().__init__()

        self.image = pygame.image.load("Libary/Images/alien.png").convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

    def update(self):
        '''Allows the alien to move across the screen'''
        if self.rect.x >= 1000:
            self.rect.x = -70
        self.rect.x += 1

        if random.randint(0, 3000) == 42:
            self.shoot()

        return

    def shoot(self):
        '''Makes the align fire a laser then will interact with shilds and the player'''
        print("\"Pew!\" said an alien")
        return

    def die(self):
        '''If the alien is hit by the player it will explode'''
        return
