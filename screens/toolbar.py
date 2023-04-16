# import libraries
import pygame
import sys
import json
import os

pygame.init()

sys.path.insert(0, "..")

# importing constants from config.py file
from config import *


images = []

folderDir = f"{os.getcwd()}/imgs/tools"

for imgs in os.listdir(folderDir):
    img = pygame.image.load(f"{folderDir}/{imgs}")
    images.append(img)

bgCol = BLACK

# toolbar screen 
def toolbarScreen():
    WIDTH = 1280
    HEIGHT = 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Toolbar Menu")

    running = True

    screen.fill(WHITE)

    ### icons
    iconSize = HEIGHT // 3
    # Pencil Icon
    pencilCoor = 20

    pencilRect = pygame.Rect(pencilCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, pencilRect, 1)
    pencilImg = pygame.image.load("imgs/tools/3.png")
    pencilImg = pygame.transform.scale(pencilImg, (iconSize - 10, iconSize - 10))
    screen.blit(pencilImg, (pencilCoor + 5,  25))

    # Pen/Paintbrush
    penCoor = 20 * 2 + iconSize

    penRect = pygame.Rect(penCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, penRect, 1)
    pencilPNG = pygame.image.load("imgs/tools/0.png")
    pencilPNG = pygame.transform.scale(pencilPNG, (iconSize - 10, iconSize - 10))
    screen.blit(pencilPNG, (penCoor + 5, 25))

    # alphabrush
    alphaCoor = 20 * 3 + iconSize * 2
    alphaRect = pygame.Rect(alphaCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, alphaRect, 1)
    alphaImg = pygame.image.load("imgs/tools/2.png")
    alphaImg = pygame.transform.scale(alphaImg, (iconSize - 10, iconSize - 10))
    screen.blit(alphaImg, (alphaCoor + 5, 25))

    # erasor
    erasorCoor = 20 * 4 + iconSize * 3
    erasorRect = pygame.Rect(erasorCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, erasorRect, 1)
    erasorImg = pygame.image.load("imgs/tools/1.png")
    erasorImg = pygame.transform.scale(erasorImg, (iconSize - 10, iconSize - 10))
    screen.blit(erasorImg, (erasorCoor + 5, 25))

    # spraycan
    sprayCoor = 20 * 5 + iconSize * 4
    sprayRect = pygame.Rect(sprayCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, sprayRect, 1)
    sprayImg = pygame.image.load("imgs/tools/4.png")
    sprayImg = pygame.transform.scale(sprayImg, (iconSize - 10, iconSize - 10))
    screen.blit(sprayImg, (sprayCoor + 5, 25))

    # line
    lineCoor = 20 * 6 + iconSize * 5
    lineRect = pygame.Rect(lineCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, lineRect, 1)
    lineImg = pygame.image.load("imgs/tools/5.png")
    lineImg = pygame.transform.scale(lineImg, (iconSize - 10, iconSize - 10))
    screen.blit(lineImg, (lineCoor + 5, 25))

    # rectangle
    rectangleCoor = 20 * 7 + iconSize * 6
    rectangleRect = pygame.Rect(rectangleCoor, 20, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, rectangleRect, 1)
    rectangleImg = pygame.image.load("imgs/tools/6.png")
    rectangleImg = pygame.transform.scale(rectangleImg, (iconSize - 10, iconSize - 10))
    screen.blit(rectangleImg, (rectangleCoor + 5, 25))

    # circle
    circleCoor = 20 * 1 + iconSize * 0
    circleRect = pygame.Rect(circleCoor, 20  + HEIGHT // 2, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, circleRect, 1)
    circleImg = pygame.image.load("imgs/tools/7.png")
    circleImg = pygame.transform.scale(circleImg, (iconSize - 10, iconSize - 10))
    screen.blit(circleImg, (circleCoor + 5, 25  + HEIGHT // 2))

    # eyeDropper
    eyeDropperCoor = 20 * 2 + iconSize * 1
    eyeDropperRect = pygame.Rect(eyeDropperCoor, 20 + HEIGHT // 2, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, eyeDropperRect, 1)
    eyeDropperImg = pygame.image.load("imgs/tools/8.png")
    eyeDropperImg = pygame.transform.scale(eyeDropperImg, (iconSize - 10, iconSize - 10))
    screen.blit(eyeDropperImg, (eyeDropperCoor + 5, 25 + HEIGHT // 2))

    # fill
    fillCoor = 20 * 3 + iconSize * 2
    fillRect = pygame.Rect(fillCoor, 20 + HEIGHT // 2, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, fillRect, 1)
    fillImg = pygame.image.load("imgs/tools/9.png")
    fillImg = pygame.transform.scale(fillImg, (iconSize - 10, iconSize - 10))
    screen.blit(fillImg, (fillCoor + 5, 25 + HEIGHT // 2))

    # text ??
    textCoor = 20 * 4 + iconSize * 3
    textRect = pygame.Rect(textCoor, 20 + HEIGHT // 2, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, textRect, 1)
    textImg = pygame.image.load("imgs/tools/10.png")
    textImg = pygame.transform.scale(textImg, (iconSize - 10, iconSize - 10))
    screen.blit(textImg, (textCoor + 5, 25 + HEIGHT // 2))

    # undo
    undoCoor = 20 * 5 + iconSize * 4
    undoRect = pygame.Rect(undoCoor, 20 + HEIGHT // 2, iconSize, iconSize)
    pygame.draw.rect(screen, BLACK, undoRect, 1)
    undoImg = pygame.image.load("imgs/tools/14.png")
    undoImg = pygame.transform.scale(undoImg, (iconSize - 10, iconSize - 10))
    screen.blit(undoImg, (undoCoor + 5, 25 + HEIGHT // 2))

    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # for i in range(len(images)):
        #     if i < len(images) / 2 - 1:
        #         screen.blit(images[i], (60*i, 0))
        #     else:
        #         screen.blit(images[i], (60*(i-(len(images)+1)/2), images[i].get_height()))
    
        pygame.display.flip()
