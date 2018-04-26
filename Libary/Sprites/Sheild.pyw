import pygame


class Player(pygame.sprite.Sprite):
    '''This class repersents the sheild that help the player'''

    def __init__(self):
        '''Sets up the player's ship'''

        super().__init__()

        self.image = pygame.image.load("Libary/Images/player.png").convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

    def update(self):
        '''Allows the player to move across the screen using mouse co-ords'''
        return

    def shoot(self):
        '''Makes the player fire a laser then will interact with shilds and the aliens'''
        return

    def die(self):
        '''If the player is hit by the alien they will explode and game over'''
        return
