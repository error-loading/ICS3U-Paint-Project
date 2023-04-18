# import libraries
import pygame
import sys
import json
import os
import multiprocessing
from tkinter import *
from tkinter import filedialog

Tk().withdraw() #hides the small extra window

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
from utils.Lines import Line
from utils.Erasor import Erasor
from utils.Save import Save
from utils.Text import Text


# parsing the json file
with open("config.json") as json_file:
    data = json.load(json_file)

# saving the data gotten form the json file in variables to use later
tool = data["tool"]
colour = tuple(map(int, data["colour"].strip("()").split(", ")))
size = int(data["size"])
opacity = data["opacity"]
gridDraw = data["gridDraw"]

# def receive_data():
#     with multiprocessing.Manager() as manager:
#         shared_data = manager.dict()
#         # do something with shared_data, such as retrieve it from a multiprocessing process
#         return dict(shared_data)

def update():
    try:
        with open("config.json") as json_file:
            # print('o')
            data = json.load(json_file)

            # print(data)

            tool = data["tool"]
            colour = tuple(map(int, data["colour"].strip("()").split(", ")))
            size = int(data["size"])
            opacity = data["opacity"]
            gridDraw = data["gridDraw"]
            undoStatus = data["undoStatus"]
            screenShot = data["screenShot"]

            returnUser = [tool, colour, size, opacity, gridDraw, undoStatus, screenShot]
            if returnUser == None:
                return ["", "", "", "", "", ""]

            return [tool, colour, size, opacity, gridDraw, undoStatus, screenShot]
    except:
        pass

# def update():
#     data = receive_data()

#     # print(data)

#     tool = data["tool"]
#     colour = tuple(map(int, data["colour"].strip("()").split(", ")))
#     size = int(data["size"])
#     opacity = data["opacity"]
#     gridDraw = data["gridDraw"]
#     undoStatus = data["undoStatus"]
#     screenShot = data["screenShot"]

#     returnUser = [tool, colour, size, opacity, gridDraw, undoStatus, screenShot]
#     if returnUser == None:
#         return ["", "", "", "", "", ""]

#     return [tool, colour, size, opacity, gridDraw, undoStatus, screenShot]


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

    tool, colour, size, opacity, gridDraw, undoStatus, screenShot = update()


    # instatiate class objects
    alphaBrush = AlphaBrush(bg, (0,255,0,12), colourErase, size, opacity)
    grd = Grid(bg, 720, 1280, colour)
    pb = Paintbrush(bg, size, colour, BLACK, 0)
    pencil = Pencil(bg, colour, size)
    rectangle = Rectangle(screen, colour, -1, -1)
    ellipse = Ellipse(screen, colour, -1, -1)
    line = Line(screen, colour, -1, -1)
    erase = Erasor(screen, size, BLACK)
    save = Save(screen)
    text = Text(screen)

    mx, my = 0, 0

    undo.append(bg)

    while running:
        screen.fill(BLACK)
        screen.blit(undo[-1], (0, 0))

        tool, colour, size, opacity, gridDraw, undoStatus, screenShot = list(update())

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT: # quits the process upon being quit
                running = False
            
            if evt.type == pygame.MOUSEBUTTONUP:
                bgImg = screen.copy()
                undo.append(bgImg)

                if tool == "text":
                    text.draw(mx, my, size, colour)
                
                elif tool == "Rectangle":
                    rectangle.firstClicked = True
                    bgImg = rectangle.drawPer(mx, my)
                    undo.append(bgImg)
                
                elif tool == "ellipse":
                    ellipse.firstClicked = True
                    bgImg = ellipse.drawPer(mx, my)
                    undo.append(bgImg)

                elif tool == "line":
                    line.firstClicked = True
                    bgImg = line.drawPer(mx, my)
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
                bgImg = screen.copy()
                undo.append(bgImg)
            
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
                
            elif tool == "line":
                if line.firstClicked:
                    line.omx = mx
                    line.omy = my
                    line.firstClicked = False

                line.draw(mx, my)
            
            elif tool == "erasor":
                erase.erase(mx, my)
        

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
        
        if undoStatus:
            imgBack = undo.pop()
            redo.append(imgBack)

            with open("config.json") as f:
                data = json.load(f)

                open('config.json', 'w').close()

                data["undoStatus"] = False

                with open("config.json", "w") as f:
                    json.dump(data, f)
        
        if screenShot:
            save.ask()

            with open("config.json") as f:
                data = json.load(f)

                open('config.json', 'w').close()

                data["screenShot"] = False

                with open("config.json", "w") as f:
                    json.dump(data, f)
            
        # update class parameters, should hv been a method parameter
        grd.col = colour
        pb.colour = colour
        pencil.colour = colour
        rectangle.colour = colour
        ellipse.colour = colour
        line.colour = colour
        

        pygame.display.flip()
