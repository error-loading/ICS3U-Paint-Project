# import libraries
import pygame
from config import *
from tkinter import filedialog
import tkinter as tk
import sys


# change the path to root of directory 
sys.path.insert(0, "..")

# import class
from utils.Stamps import Stamps

# importing constants from config.py file
from config import *

# initialize pygame module
pygame.init()

def sticker():
    # screen info constants
    WIDTH = 225
    HEIGHT = 800

    # initializing screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Stamps Menu")

    # screen info variables
    running = True
    drawing = False
    ogBack = screen.copy()
    back = screen.copy()

    firstIter = True


    while running:
        # fill the background
        if drawing:
            screen.blit(back, (0, 0))

        # Stamp 1
        sport1 = Stamps(screen, 0, 0, WIDTH, "imgs/stamps/sport1.png")

        # Stamp 2
        sport2 = Stamps(screen, 0, sport1.img.get_height(), WIDTH, "imgs/stamps/sport2.png")

        # Stamp 3
        sport3 = Stamps(screen, 0, sport2.boxRect.bottomleft[1], WIDTH, "imgs/stamps/sport3.png")

        # Stamp 4
        sport4 = Stamps(screen, 0, sport3.boxRect.bottomleft[1], WIDTH, "imgs/stamps/sport4.png")

        # Stamp 5
        sport5 = Stamps(screen, 0, sport4.boxRect.bottomleft[1], WIDTH, "imgs/stamps/sport5.png")


        if firstIter:
            ogBack = screen.copy()
            firstIter = False 

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False
            
            elif evt.type == pygame.MOUSEBUTTONUP:
                screen.blit(ogBack, (0, 0))
                if sport1.boxRect.collidepoint(pygame.mouse.get_pos()):
                    sport1.tool_name("stamp1")
                    back = sport1.draw_clicked(YELLOW, 3)

                elif sport2.boxRect.collidepoint(pygame.mouse.get_pos()):
                    sport2.tool_name("stamp2")
                    back = sport2.draw_clicked(YELLOW, 3)

                elif sport3.boxRect.collidepoint(pygame.mouse.get_pos()):
                    sport3.tool_name("stamp3")
                    back = sport3.draw_clicked(YELLOW, 3)

                elif sport4.boxRect.collidepoint(pygame.mouse.get_pos()):
                    sport4.tool_name("stamp4")
                    back = sport4.draw_clicked(YELLOW, 3)

                elif sport5.boxRect.collidepoint(pygame.mouse.get_pos()):
                    sport5.tool_name("stamp5")
                    back = sport5.draw_clicked(YELLOW, 3)

                drawing = True
        
        
        # hover over rects
        if sport1.boxRect.collidepoint(pygame.mouse.get_pos()):
            sport1.draw_hover(DARKBLUE)

        elif sport2.boxRect.collidepoint(pygame.mouse.get_pos()):
            sport2.draw_hover(DARKBLUE)

        elif sport3.boxRect.collidepoint(pygame.mouse.get_pos()):
            sport3.draw_hover(DARKBLUE)
        
        elif sport4.boxRect.collidepoint(pygame.mouse.get_pos()):
            sport4.draw_hover(DARKBLUE)
        
        elif sport5.boxRect.collidepoint(pygame.mouse.get_pos()):
            sport5.draw_hover(DARKBLUE)
        
        pygame.display.flip()

    
    pygame.quit()