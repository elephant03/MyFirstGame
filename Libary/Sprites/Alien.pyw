import pygame

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
        return

    def shoot(self):
        '''Makes the align fire a laser then will interact with shilds and the player'''
        return

    def die(self):
        '''If the alien is hit by the player it will explode'''
        return
