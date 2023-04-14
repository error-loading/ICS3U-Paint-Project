import pygame
from config import *

pygame.init()

# import classes from utils folder

from ..utils.Fill import Fill

# main screen for canvas
def mainScreen():
    running = True 
    screen = pygame.display.set_mode((1280, 720))
    screen.fill(WHITE)
    pygame.display.set_caption("Whiteboard")


    while running:

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT: # quits the process upon being quit
                running = False


        pygame.display.flip()