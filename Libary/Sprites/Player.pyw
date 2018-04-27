import pygame

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    '''This class repersents the player and can move'''

    def __init__(self):
        '''Sets up the player's ship'''

        super().__init__()

        self.image = pygame.image.load("Libary/Images/player.png").convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

    def update(self):
        '''Allows the player to move across the screen using mouse co-ords'''
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        return

    def die(self):
        '''If the player is hit by the alien they will explode and game over'''
        return
