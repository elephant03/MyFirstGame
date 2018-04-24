import pygame


class Alien(pygame.sprite.Sprite):
    '''This class repersents the aliens on screen'''

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Libary/Images/alien.png").convert()
