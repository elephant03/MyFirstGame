import pygame

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Sheild(pygame.sprite.Sprite):
    '''This class repersents the sheild that help the player'''

    def __init__(self):
        '''Sets up the player's sheild'''

        super().__init__()

        self.image = pygame.image.load("Libary/Images/sheild.png").convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.lives = 5

    def update(self):
        return

    def hit(self):
        '''will subtract a life and destroy the sheild if it gets too damaged'''
        return

    def die(self):
        '''Destroys the sheild'''
        return
