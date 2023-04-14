import pygame
import sys

sys.path.insert(0,"..")

WHITE = (255, 255, 255)

pygame.init()

# import classes from utils folder

from utils.Fill import Fill
from utils.AlphaBrush import AlphaBrush



# main screen for canvas
def mainScreen(tool, colour, size, opacity):
    running = True 
    screen = pygame.display.set_mode((1280, 720))
    screen.fill(WHITE)
    pygame.display.set_caption("Whiteboard")


    # instatiate class objects
    alphaBrush = AlphaBrush(screen, colour, size, opacity)

    while running:

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT: # quits the process upon being quit
                running = False

        mb = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if mb[0]:
            if tool == "alphaBrush":
                alphaBrush.draw(mx, my)
        elif mb[2]:
            if tool == "alphaBrush":
                alphaBrush.erase(mx, my)
                    


        pygame.display.flip()