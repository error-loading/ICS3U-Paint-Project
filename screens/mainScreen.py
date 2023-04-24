# import libraries
import pygame
import sys
import json
import os
import multiprocessing
from tkinter import *
from tkinter import filedialog

# change the path to make it easier to import classes
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
from utils.Eyedropper import Eyedropper
from utils.Load import Load
from utils.StampImg import StampImg

# import config.py for a few constants shared across multiple files
from config import *


## Intialize modules

# Intialize the tk module and then hide the small extra window
Tk().withdraw()

# Intialize the pygame module
pygame.init()


# update function that updates values taken from the config.json file

def update():
    # load the config.json file
    with open("config.json") as json_file:
        data = json.load(json_file)

    if data:
        # parse the json file
        tool = data["tool"]
        colour = tuple(map(int, data["colour"].strip("()").split(", ")))
        size = int(data["size"])
        opacity = data["opacity"]
        gridDraw = data["gridDraw"]
        undoStatus = data["undoStatus"]
        screenShot = data["screenShot"]
        redoStatus = data["redoStatus"]
        load = data["load"]


        # return values taken from json file
        returnUser = [tool, colour, size, opacity, gridDraw, undoStatus, screenShot, redoStatus, load]

        return returnUser
    
    else:
        returnUser = ["pb", (130, 80, 167), 5, "5", False, False, False, False, False]

        return returnUser



# main screen process for canvas
def mainScreen():
    ## any variables that might be needed

    # make these variables global for later usage and just to be careful of any issues
    tool, colour, size, opacity, gridDraw, undoStatus, screenShot, redoStatus, load = update()

    # undo/redo lists
    undo = []
    redo = []

    # background colour
    bgCol = (40, 40, 40)

    WIDTH = 1280
    HEIGHT = 720

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(bgCol)
    pygame.display.set_caption("Whiteboard")

    running = True

    # instatiate class objects
    pb = Paintbrush(screen, size, colour, bgCol, 0)
    alphaBrush = AlphaBrush(screen, tuple(list(colour) + [int(opacity)]), bgCol, size, 0)
    pencil = Pencil(screen, colour, size)
    erasor = Erasor(screen, size, bgCol)
    line = Line(screen, colour, -1, -1, size)
    rectangle = Rectangle(screen, colour, -1, -1, size)
    ellipse = Ellipse(screen, colour, -1, -1, size)
    eyeDropper = Eyedropper()
    fill = Fill(screen, colour)
    text = Text(screen)
    save = Save(screen)
    loadOb = Load(screen)

    # class objects for stamps
    stamp1 = StampImg(screen, -1, -1, "imgs/stamps/sport1.png")
    stamp2 = StampImg(screen, -1, -1, "imgs/stamps/sport2.png")
    stamp3 = StampImg(screen, -1, -1, "imgs/stamps/sport3.png")
    stamp4 = StampImg(screen, -1, -1, "imgs/stamps/sport4.png")
    stamp5 = StampImg(screen, -1, -1, "imgs/stamps/sport5.png")



    # give undo list starting image
    back = screen.copy()
    undo.append(back)

    # mouse x and mouse y
    mx, my = 0, 0

    # if the user is currently drawing
    drawing = False

    # pygame loop
    while running:
        # fill the screen with the latest image in undo list if the user is not drawing
        if not drawing:
            screen.blit(undo[-1], (0, 0))

        # event loop
        for evt in pygame.event.get():

            # if the user exits out, close the pygame window
            if evt.type == pygame.QUIT:
                running = False

            # first iteration of user pressing mouse
            elif evt.type == pygame.MOUSEBUTTONDOWN:
                if tool == "eyeDropper":
                    eyeDropper.drop(mx, my, screen)

                elif tool == "fill":
                    fill.fill(mx, my)
                    bgImg = screen.copy()
                    undo.append(bgImg)

       

            # first iteration of user letting go of mouse
            elif evt.type == pygame.MOUSEBUTTONUP:
                # change the state of the painbrush (0 for first clicked and 1 for everything else)
                if tool == "pb":
                    pb.state = 0

                elif tool == "alphaBrush":
                    alphaBrush.state = 0

                elif tool == "line":
                    line.firstClicked = True
                    line.drawPer(mx, my)
                
                elif tool == "rectangle":
                    rectangle.firstClicked = True
                    rectangle.drawPer(mx, my)

                elif tool == "ellipse":
                    ellipse.firstClicked = True
                    ellipse.drawPer(mx, my)

                elif tool == "text":
                    txt = text.getName(mx, my)
                    comicFont = pygame.font.SysFont("Comic Sans MS", size)
                    txtPic = comicFont.render(txt, True, colour)
                    screen.blit(txtPic,(mx,my))

                elif tool == "stamp1":
                    stamp1.firstClicked = True
                    stamp1.drawPer(mx, my)

                elif tool == "stamp2":
                    stamp2.firstClicked = True
                    stamp2.drawPer(mx, my)

                elif tool == "stamp3":
                    stamp3.firstClicked = True
                    stamp3.drawPer(mx, my)

                elif tool == "stamp4":
                    stamp4.firstClicked = True
                    stamp4.drawPer(mx, my)

                elif tool == "stamp5":
                    stamp5.firstClicked = True
                    stamp5.drawPer(mx, my)

                     

                # append img to back of undo list
                bgImg = screen.copy()
                undo.append(bgImg)
        
                # drawing ends here
                drawing = False

        # mouse interactions
        mb = pygame.mouse.get_pressed()
        omx, omy = mx, my
        mx, my = pygame.mouse.get_pos()

        # if the left mouse is held
        if mb[0]:
            # look at what tool is selected, and display it on canvas
            if tool == "pb":
                pb.draw(mx, my)
                # the user is currently drawing
                drawing = True
            
            elif tool == "alphaBrush" and (mx!=omx or my!=omy):
                alphaBrush.draw(mx, my)
                # the user is currently drawing
                drawing = True
            
            elif tool == "pencil":
                pencil.draw(omx, omy, mx, my)
                # the user is currently drawing
                drawing = True
            
            elif tool == "erasor":
                erasor.erase(mx, my)
                # the user is currently drawing
                drawing = True

            elif tool == "line":
                if line.firstClicked:
                    line.omx = mx
                    line.omy = my
                    line.firstClicked = False

                line.draw(mx, my)
            
            elif tool == "rectangle":
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

            elif tool == "stamp1":
                if stamp1.firstClicked:
                    stamp1.omx = mx
                    stamp1.omy = my
                    stamp1.firstClicked = False

                stamp1.draw(mx, my)

            elif tool == "stamp2":
                if stamp2.firstClicked:
                    stamp2.omx = mx
                    stamp2.omy = my
                    stamp2.firstClicked = False

                stamp2.draw(mx, my)

            elif tool == "stamp3":
                if stamp3.firstClicked:
                    stamp3.omx = mx
                    stamp3.omy = my
                    stamp3.firstClicked = False

                stamp3.draw(mx, my)

            elif tool == "stamp4":
                if stamp4.firstClicked:
                    stamp4.omx = mx
                    stamp4.omy = my
                    stamp4.firstClicked = False

                stamp4.draw(mx, my)

            elif tool == "stamp5":
                if stamp5.firstClicked:
                    stamp5.omx = mx
                    stamp5.omy = my
                    stamp5.firstClicked = False

                stamp5.draw(mx, my)
        

            
            

        
        # if the right mouse is held
        elif mb[2]:
            if tool == "pb":
                pb.erase(mx, my)
            
            if tool == "alphaBrush":
                alphaBrush.erase(mx, my)
            
            if tool == "pencil":
                pencil.erase(mx, my)
            
            # erasing counts as drawing ykyk
            drawing = True


        # code for undo
        if undoStatus:
            # make sure your not popping from an empty list
            if len(undo) > 1:
                imgBack = undo.pop()
                redo.append(imgBack)

                with open("config.json") as f:
                    data = json.load(f)

                data["undoStatus"] = False

                with open("config.json", "w") as f:
                    json.dump(data, f)

        # code for redo
        if redoStatus:
            # make sure if there is an item in redo list
            if len(redo):
                redoBack = redo.pop()
                undo.append(redoBack)
    
                with open("config.json") as f:
                    data = json.load(f)

                data["redoStatus"] = False

                with open("config.json", "w") as f:
                    json.dump(data, f)
        

        # if user presses screeshot
        if screenShot:
            save.ask()

            # reset the value in the json file
            with open("config.json") as f:
                data = json.load(f)


            data["screenShot"] = False

            with open("config.json", "w") as f:
                json.dump(data, f)
        
        # if user presses load bitmap
        if load:
            fname = loadOb.ask()
            if fname:
                loadBgImg = pygame.image.load(fname)
                undo.append(loadBgImg)


            # reset the value in the json file
            with open("config.json") as f:
                data = json.load(f)


            data["load"] = False

            with open("config.json", "w") as f:
                json.dump(data, f)

        
        # update all these variables
        tool, colour, size, opacity, gridDraw, undoStatus, screenShot, redoStatus, load = list(update())

        # update class parameters, should hv been method parameters but too late now
        pb.colour = colour
        pb.size = size

        alphaBrush.colour = colour
        alphaBrush.size = size
    
        pencil.colour = colour
        pencil.size = size

        erasor.size = size

        line.size = size
        line.colour = colour

        rectangle.colour = colour
        rectangle.size = size

        ellipse.colour = colour
        ellipse.size = size
        # flip the changes to the canvas
        pygame.display.flip()
    



    # quit the pygame module
    pygame.quit()
