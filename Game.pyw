# Attempt to import the pygame libary
try:
    import pygame
except ImportError:
    # If it fails it will exit the program and give an error
    print("Cannot load pygame.\nPlease check that it installed and try again.")
    raise SystemExit

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

# Creats varbles used in the entire program

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimentions
screen_width = 1000
screen_height = 500
screen_size = (screen_width, screen_height)

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

        self.game_over = False

        # Create sprite lists
        self.alien_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for x in range(70, screen_width-105, 140):
            for y in range(50, int(screen_height/2)+50, 80):
                alien = Alien.Alien()

                alien.rect.x = x
                alien.rect.y = y

                self.alien_list.add(alien)
                self.all_sprites_list.add(alien)

        for x in range(40, screen_width, 100):

        print(len(self.all_sprites_list))

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # At the end of the game a "click to restart" will apear that will run this code
            if self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                self.__init__()

        return False

    def run_logic(self):
        '''Controls the movement and collisions of all of the sprites'''
        return

    def display_frame(self, screen):
        '''Redraws the pygame window from there possitons'''
        # clears the screen
        screen.fill(WHITE)

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
    screen = pygame.display.set_mode(screen_size, 0)

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
