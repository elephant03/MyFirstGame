'''
See README.md for details or visit
'''

try:
    import pygame
    from pygame.locals import *
except ImportError:
    try:
        import tkinter as TK
        root = TK.Tk()
        Lbl = TK.Label(
            root, text="Sorry but you must have pygame installed to run this program\nPlease see the README for more details")
        Lbl.pack(fill=TK.BOTH, expand=True)
        raise SystemExit
    except:
        print("We are sorry but you don't seem to have pygame installed and so this program cannot run\nPlease see the README for more details")
        raise SystemExit


class Main():
    '''
    The main class of the game containing the game loop and event handelers
    '''

    # Sets up key common varables
    FPS = 30  # frames per second setting
    FPSClock = pygame.time.Clock()

    def __init__(self):
        pygame.init()

        self.DisplayScreen = pygame.display.set_mode((300, 400), 0)

        # The main game loop
        while True:
            self.EventHandeler()

            self.FPSClock.tick(self.FPS)

    def EventHandeler(self):
        '''
        Gose through all of the events in the queue and runs the neccessary event
        '''
        for event in pygame.event.get():
            # Exits the program if the quit event is called
            if event.type == QUIT:
                raise SystemExit

            print(event)


def Run(_PlaceHolder):
    Main()


if __name__ == "__main__":
    Main()
