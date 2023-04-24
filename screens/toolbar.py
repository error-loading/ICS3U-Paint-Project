# import libraries
import pygame
import sys
import json
import os
import tkinter as tk
from tkinter.colorchooser import askcolor


# change the path to root of directory 
sys.path.insert(0, "..")

# import RectImgs class
from utils.RectImgs import RectImgs
from utils.Slider import Slider

# importing constants from config.py file
from config import *

# initialize pygame module
pygame.init()

def toolbarScreen():
    # screen info constants
    WIDTH = 1280
    HEIGHT = 200

    # initializing screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Toolbar Menu")

    # instatiate stuff
    slider = Slider(20 * 8 + HEIGHT // 3 * 7, 20 + HEIGHT // 2, 1230 - 20 * 8 - HEIGHT // 3 * 7, HEIGHT // 3)

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

        ### icons
        iconSize = HEIGHT // 3

        # Pencil Icon
        pencilCoor = 20
        pencilOb = RectImgs(screen, pencilCoor, 20, iconSize, 3)

        # Pen/Paintbrush
        penCoor = 20 * 2 + iconSize
        penOb = RectImgs(screen, penCoor, 20, iconSize, 0)

        # alphaBrush
        alphaCoor = 20 * 3 + iconSize * 2
        alphaOb = RectImgs(screen, alphaCoor, 20, iconSize, 2)

        # erasor
        erasorCoor = 20 * 4 + iconSize * 3
        erasorOb = RectImgs(screen, erasorCoor, 20, iconSize, 1)

        # loadCan
        loadCoor = 20 * 5 + iconSize * 4
        loadOb = RectImgs(screen, loadCoor, 20, iconSize, 19)

        # lines
        lineCoor = 20 * 6 + iconSize * 5
        lineOb = RectImgs(screen, lineCoor, 20, iconSize, 5)
    
        # rectangle
        rectangleCoor = 20 * 7 + iconSize * 6
        rectangleOb = RectImgs(screen, rectangleCoor, 20, iconSize, 6)
    
        # circle
        circleCoor = 20 * 1 + iconSize * 0
        circleOb = RectImgs(screen, circleCoor, 20  + HEIGHT // 2, iconSize, 7)

        # eyeDropper
        eyeCoor = 20 * 2 + iconSize * 1
        eyeOb = RectImgs(screen, eyeCoor, 20 + HEIGHT // 2, iconSize, 8)

        # fill
        fillCoor = 20 * 3 + iconSize * 2
        fillOb = RectImgs(screen, fillCoor, 20 + HEIGHT // 2, iconSize, 9)

        # text
        textCoor = 20 * 4 + iconSize * 3
        textOb = RectImgs(screen, textCoor, 20 + HEIGHT // 2, iconSize, 10)

        # undo
        undoCoor = 20 * 5 + iconSize * 4
        undoOb = RectImgs(screen, undoCoor, 20 + HEIGHT // 2, iconSize, 14)

        # redo
        redoCoor = 20 * 6 + iconSize * 5
        redoOb = RectImgs(screen, redoCoor, 20 + HEIGHT // 2, iconSize, 15)

        # save
        saveCoor = 20 * 7 + iconSize * 6
        saveOb = RectImgs(screen, saveCoor, 20 + HEIGHT // 2, iconSize, 17)
    
        # colour map

        colourCoor = 20 * 8 + iconSize * 7
        colourOb = RectImgs(screen, colourCoor, 20, iconSize, 18)

        selectColourRect = pygame.Rect(730, 20, 500, HEIGHT // 3)

        with open("config.json") as f:
            data = json.load(f)

        
        # the colour tuple is in a string, this code decodes that back into a normal python tuple
        colour = tuple(map(int, data["colour"].strip("()").split(", ")))


        pygame.draw.rect(screen, colour, selectColourRect)
    



        if firstIter:
            ogBack = screen.copy()
            firstIter = False 

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False
            
            elif evt.type == pygame.MOUSEBUTTONUP:
                screen.blit(ogBack, (0, 0))
                if pencilOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    pencilOb.tool_name("pencil")
                    back = pencilOb.draw_clicked(YELLOW, 3)
                
                elif penOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    penOb.tool_name("pb")
                    back = penOb.draw_clicked(YELLOW, 3)

                elif alphaOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    alphaOb.tool_name("alphaBrush")
                    back = alphaOb.draw_clicked(YELLOW, 3)

                elif erasorOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    erasorOb.tool_name("erasor")
                    back = erasorOb.draw_clicked(YELLOW, 3)
                
                elif loadOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    loadOb.tool_status("load")
                    back = loadOb.draw_clicked(YELLOW, 3)
                    
                elif lineOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    lineOb.tool_name("line")
                    back = lineOb.draw_clicked(YELLOW, 3)
                    
                elif rectangleOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    rectangleOb.tool_name("rectangle")
                    back = rectangleOb.draw_clicked(YELLOW, 3)
                    
                elif circleOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    circleOb.tool_name("ellipse")
                    back = circleOb.draw_clicked(YELLOW, 3)
                
                elif eyeOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    eyeOb.tool_name("eyeDropper")
                    back = eyeOb.draw_clicked(YELLOW, 3)
                    
                elif fillOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    fillOb.tool_name("fill")
                    back = fillOb.draw_clicked(YELLOW, 3)
                    
                elif textOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    textOb.tool_name("text")
                    back = textOb.draw_clicked(YELLOW, 3)
                    
                elif undoOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    undoOb.tool_status("undoStatus")
                    back = undoOb.draw_clicked(YELLOW, 3)
                    
                elif redoOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    redoOb.tool_status("redoStatus")
                    back = redoOb.draw_clicked(YELLOW, 3)
                
                elif saveOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    saveOb.tool_status("screenShot")
                    back = saveOb.draw_clicked(YELLOW, 3)
                
                elif colourOb.boxRect.collidepoint(pygame.mouse.get_pos()):
                    newColour = askcolor()[0]

                    if newColour != "":
                        with open("config.json") as f:
                            data = json.load(f)


                        data['colour'] = str(newColour)

                        with open("config.json", "w") as f:
                            json.dump(data, f)          




                drawing = True

                    # Pass events to the slider object to handle
        
            slider.handle_event(evt)

        # Draw the slider on the screen
        slider.draw(screen)
        
        
        # hover over rects
        if pencilOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            pencilOb.draw_hover(DARKBLUE)
        
        elif penOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            penOb.draw_hover(DARKBLUE)
        
        elif alphaOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            alphaOb.draw_hover(DARKBLUE)
        
        elif erasorOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            erasorOb.draw_hover(DARKBLUE)
        
        elif loadOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            loadOb.draw_hover(DARKBLUE)
        
        elif lineOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            lineOb.draw_hover(DARKBLUE)
        
        elif rectangleOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            rectangleOb.draw_hover(DARKBLUE)
        
        elif circleOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            circleOb.draw_hover(DARKBLUE)
        
        elif eyeOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            eyeOb.draw_hover(DARKBLUE)
        
        elif fillOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            fillOb.draw_hover(DARKBLUE)
        
        elif textOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            textOb.draw_hover(DARKBLUE)
        
        elif undoOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            undoOb.draw_hover(DARKBLUE)
        
        elif redoOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            redoOb.draw_hover(DARKBLUE)

        elif saveOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            saveOb.draw_hover(DARKBLUE)
        
        elif colourOb.boxRect.collidepoint(pygame.mouse.get_pos()):
            colourOb.draw_hover(DARKBLUE)


        
        pygame.display.flip()

    
    pygame.quit()