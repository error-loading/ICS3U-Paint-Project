# import libraries
import pygame
import sys
import json
import os

# intialize the pygame module
pygame.init()

# import config.py for a few constants shared across multiple files
from config import *


# change the path to make it easier to import classes
curPath = os.getcwd()
sys.path.insert(0, f'{curPath}/utils')

# import classes from utils folder
from Fill import Fill
from AlphaBrush import AlphaBrush
from Grid import Grid
from Paintbrush import Paintbrush
from Pencil import Pencil


# parsing the json file
with open("config.json") as json_file:
    data = json.load(json_file)

# saving the data gotten form the json file in variables to use later
tool = data["tool"]
colour = tuple(map(int, data["colour"].strip("()").split(", ")))
size = int(data["size"])
opacity = data["opacity"]
gridDraw = data["gridDraw"]

colourErase = BLACK

# main screen for canvas
def mainScreen():
    running = True 
    screen = pygame.display.set_mode((1280, 720))
    pygame.draw.line(screen, BLUE, (10, 0), (10, 800), 1)
    bg = pygame.Surface((1280, 720))
    pygame.display.set_caption("Whiteboard")


    # instatiate class objects
    alphaBrush = AlphaBrush(bg, (0,255,0,12), colourErase, size, opacity)
    grd = Grid(bg, 720, 1280, colour)
    pb = Paintbrush(size, colour, BLACK, 0, bg)
    pencil = Pencil(bg, colour, size)

    mx, my = 0, 0

    while running:
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))
        if gridDraw:
            grd.on()


        for evt in pygame.event.get():
            if evt.type == pygame.QUIT: # quits the process upon being quit
                running = False

        mb = pygame.mouse.get_pressed()
        omx, omy = mx, my
        mx, my = pygame.mouse.get_pos()

        if mb[0]:
            if tool == "alphaBrush" and omx!= mx and omy!=my:
                alphaBrush.draw(mx, my)
            elif tool == "pencil":
                pencil.draw(omx, omy, mx, my)

        elif mb[2]:
            if tool == "alphaBrush" and omx!= mx and omy!=my:
                alphaBrush.erase(mx, my)
            
            elif tool == "pencil":
                pencil.erase(mx, my)
                    
        pygame.display.flip()
