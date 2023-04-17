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
# curPath = os.getcwd()
# sys.path.insert(0, f'{curPath}/utils')
sys.path.insert(0, "..")

# import classes from utils folder
from utils.Fill import Fill
from utils.AlphaBrush import AlphaBrush
from utils.Grid import Grid
from utils.Paintbrush import Paintbrush
from utils.Pencil import Pencil
from utils.Rectangle import Rectangle
from utils.Ellipse import Ellipse


# parsing the json file
with open("config.json") as json_file:
    data = json.load(json_file)

# saving the data gotten form the json file in variables to use later
tool = data["tool"]
colour = tuple(map(int, data["colour"].strip("()").split(", ")))
size = int(data["size"])
opacity = data["opacity"]
gridDraw = data["gridDraw"]

def update():
    try:
        with open("config.json") as json_file:
            data = json.load(json_file)

            tool = data["tool"]
            colour = tuple(map(int, data["colour"].strip("()").split(", ")))
            size = int(data["size"])
            opacity = data["opacity"]
            gridDraw = data["gridDraw"]
            print([tool, colour, size, opacity, gridDraw])

            return [tool, colour, size, opacity, gridDraw]
    except:
        pass

colourErase = BLACK

# undo/redo lists
undo = []
redo = []

# main screen for canvas
def mainScreen():
    running = True 
    screen = pygame.display.set_mode((1280, 720))
    pygame.draw.line(screen, BLUE, (10, 0), (10, 800), 1)
    bg = pygame.Surface((1280, 720))
    pygame.display.set_caption("Whiteboard")

    tool, colour, size, opacity, gridDraw = update()


    # instatiate class objects
    alphaBrush = AlphaBrush(bg, (0,255,0,12), colourErase, size, opacity)
    grd = Grid(bg, 720, 1280, colour)
    pb = Paintbrush(bg, size, colour, BLACK, 0)
    pencil = Pencil(bg, colour, size)
    rectangle = Rectangle(screen, colour, -1, -1)
    ellipse = Ellipse(screen, colour, -1, -1)

    mx, my = 0, 0

    undo.append(bg)

    while running:
        screen.fill(BLACK)
        screen.blit(undo[-1], (0, 0))

        tool, colour, size, opacity, gridDraw = list(update())

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT: # quits the process upon being quit
                running = False
            
            if evt.type == pygame.MOUSEBUTTONUP:
                if tool == "Rectangle":
                    rectangle.firstClicked = True
                    bgImg = rectangle.drawPer(mx, my)
                    undo.append(bgImg)
                
                elif tool == "ellipse":
                    ellipse.firstClicked = True
                    bgImg = ellipse.drawPer(mx, my)
                    undo.append(bgImg)

        mb = pygame.mouse.get_pressed()
        omx, omy = mx, my
        mx, my = pygame.mouse.get_pos()


        if mb[0]:
            if tool == "alphaBrush" and omx!= mx and omy!=my:
                alphaBrush.draw(mx, my)
            elif tool == "pencil":
                pencil.draw(omx, omy, mx, my)
            elif tool == "pb":
                pb.draw(mx, my)
            elif tool == "fill":
                fill = Fill(screen, colour, screen.get_at([mx, my])[:3])
                fill.fill(mx, my)
            
            elif tool == "Rectangle":
                if rectangle.firstClicked:
                    rectangle.omx = mx
                    rectangle.omy = my
                    rectangle.firstClicked = False

                rectangle.draw(mx, my)
            elif tool == "ellipse":
                if ellipse.firstClicked:
                    ellipse.omx = mx
                    ellipse.omy = my
                    ellipse.firstClicked = False

                ellipse.draw(mx, my)
        

        elif mb[2]:
            if tool == "alphaBrush" and omx!= mx and omy!=my:
                alphaBrush.erase(mx, my)
            
            elif tool == "pencil":
                pencil.erase(mx, my)
            
            elif tool == "pb":
                pb.erase(mx, my)
            
            
            if gridDraw:
                grd.on()
                    
        if not mb[0]:
            if tool == "pb":
                pb.state = 0
                bgImg = screen.copy()
                undo.append(bgImg)

            if gridDraw:
                grd.on()
        pygame.display.flip()
