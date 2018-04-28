import pygame

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class AlienLaser(pygame.sprite.Sprite):
    '''This class repersents the lasers fired by the aliens that damage the player'''

    def __init__(self, x, y):
        '''Sets up the aliens laser'''

        super().__init__()

        self.image = pygame.image.load("Libary/Images/laser.png").convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.rect.x = x + 40
        self.rect.y = y + 50

    def update(self):
        self.rect.y += 4
        return
