# Attempt to import the pygame libary
try:
    import pygame
except ImportError:
    # If it fails it will exit the program and give an error
    print("Cannot load pygame.\nPlease check that it installed and try again.")
    raise SystemExit

import random

# Imports the alien sprite file
# Written out by editing the path as it is more relable then pythons cross file imports
import os
import sys
filename = "Libary/Sprites/Alien.pyw"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    Alien = __import__(module_name)
finally:
    sys.path[:] = path  # restore

# Imports the alien sprite file
# Written out by editing the path as it is more relable then pythons cross file imports
filename = "Libary/Sprites/Player.pyw"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    Player = __import__(module_name)
finally:
    sys.path[:] = path  # restore

# Imports the alien sprite file
# Written out by editing the path as it is more relable then pythons cross file imports
filename = "Libary/Sprites/Sheild.pyw"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    Sheild = __import__(module_name)
finally:
    sys.path[:] = path  # restore

# Imports the alien's laser sprite file
# Written out by editing the path as it is more relable then pythons cross file imports
filename = "Libary/Sprites/AlienLaser.pyw"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    AlienLaser = __import__(module_name)
finally:
    sys.path[:] = path  # restore

# Imports the players's laser sprite file
# Written out by editing the path as it is more relable then pythons cross file imports
filename = "Libary/Sprites/PlayerLaser.pyw"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    PlayerLaser = __import__(module_name)
finally:
    sys.path[:] = path  # restore

# Creats varbles used in the entire program

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimentions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# FPS rate
FPS = 60
clock = pygame.time.Clock()


class Game():
    '''This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. '''

    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """

        self.score = 0

        self.LaserCooldown = 0

        self.game_over = False

        # Create sprite lists
        # Comtains all of the aliens
        self.alien_list = pygame.sprite.Group()
        # Contains every sprite
        self.all_sprites_list = pygame.sprite.Group()
        # Contains everything the aliens can damage
        self.alien_damage_list = pygame.sprite.Group()
        # Contains everything the player can damage
        self.player_damage_list = pygame.sprite.Group()
        # Contains the players lasers
        self.player_shots_list = pygame.sprite.Group()
        # COntains the alien lasers
        self.alien_shots_list = pygame.sprite.Group()

        for x in range(70, SCREEN_WIDTH-105, 140):
            for y in range(30, int(SCREEN_HEIGHT/2)+50, 80):
                alien = Alien.Alien()

                alien.rect.x = x
                alien.rect.y = y

                self.alien_list.add(alien)
                self.player_damage_list.add(alien)
                self.all_sprites_list.add(alien)

                # print(alien.rect.x)
                # print(alien.rect.y)

        for x in range(40, SCREEN_WIDTH, 200):
            shield = Sheild.Sheild()

            shield.rect.x = x
            shield.rect.y = 370

            self.alien_damage_list.add(shield)
            self.player_damage_list.add(shield)
            self.all_sprites_list.add(shield)

        self.player = Player.Player()

        self.player.rect.x = 0
        self.player.rect.y = SCREEN_HEIGHT - 65

        self.alien_damage_list.add(self.player)
        self.all_sprites_list.add(self.player)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over and self.LaserCooldown <= 0:
                    playerlaser = PlayerLaser.PlayerLaser(
                        self.player.rect.x, self.player.rect.y)

                    self.LaserCooldown = 50

                    self.player_shots_list.add(playerlaser)
                    self.all_sprites_list.add(playerlaser)
                if self.game_over:
                    self.__init__()

            # At the end of the game a "click to restart" will apear that will run this code
            if self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                self.__init__()

        return False

    def run_logic(self):
        '''Controls the movement and collisions of all of the sprites'''

        if not self.game_over:
            self.all_sprites_list.update()

            for alien in self.alien_list:

                if random.randint(0, len(self.alien_list)*19) == 1:
                    alein_shot = AlienLaser.AlienLaser(
                        alien.rect.x, alien.rect.y)

                    self.all_sprites_list.add(alein_shot)
                    self.alien_shots_list.add(alein_shot)
            if self.LaserCooldown > 0:
                self.LaserCooldown -= 1

            # See if the players shots have collided with anything.
            for laser in self.player_shots_list:
                laser_hit_list = pygame.sprite.spritecollide(
                    laser, self.player_damage_list, False)
                for collision in laser_hit_list:
                    destroy = collision.hit()
                    if destroy:
                        self.all_sprites_list.remove(collision)
                        collision.kill()
                        if len(self.alien_list) == 0:
                            self.game_over = True
                    laser.kill()

            for laser in self.alien_shots_list:
                laser_hit_list = pygame.sprite.spritecollide(
                    laser, self.alien_damage_list, False)

                for collision in laser_hit_list:
                    destroy = collision.hit()
                    if destroy:
                        self.all_sprites_list.remove(collision)
                        collision.kill()
                        if collision == self.player:
                            self.game_over = True
                    laser.kill()

        return

    def display_frame(self, screen):
        '''Redraws the pygame window from there possitons'''
        # clears the screen
        screen.fill(WHITE)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            self.text = "Game Over, You Loose- click to restart!"
            if self.player.lives > 0:
                self.text = "You win! click to play again!"
            font = pygame.font.SysFont("Arial", 25)
            text = font.render(self.text, True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        # Draws everything to the game window in one flip
        pygame.display.flip()
        return


def Main():
    '''Calls the main program function'''

    # inisllises pygame
    pygame.init()

    # Creats the game window
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)

    pygame.display.set_caption("Alien")
    pygame.mouse.set_visible(False)

    # Create an instance of the Game class
    game = Game()

    # Main game loop
    while True:

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        # This will return true if the game is to close
        if done:
            # This will exit the main game loop
            break

        # Update object positions, check for collisions and other game logic
        game.run_logic()

        # Draw the current frame- all sprites etc. and clear the old screen
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(FPS)

    # Close window and exit
    pygame.quit()
    raise SystemExit


# Will only run the prgram if it is being directally called
if __name__ == "__main__":
    Main()
