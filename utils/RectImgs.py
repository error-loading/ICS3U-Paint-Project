'''
Gurjas Singh Dhillon

Stamps.py

this class is for adding the rects for each tool to the the toolMenu
'''

import pygame
import sys
import json

# change the path to root of directory 
sys.path.insert(0, "..")

class RectImgs:
    def __init__ (self, screen, x, y, side, imgNum):
        self.screen = screen
        self.x = x
        self.y = y
        self.side = side
        self.imgNum = imgNum

        self.boxRect = pygame.Rect(x, y, side, side)
        pygame.draw.rect(screen, (0, 0, 0), self.boxRect, 1)

        self.img = pygame.image.load(f"imgs/tools/{imgNum}.png")
        self.img = pygame.transform.scale(self.img, (side - 10, side - 10))
        
        self.screen.blit(self.img, (x+5, y+5))


    # while mouse is colliding point with the boxRect
    def draw_hover (self, col):
        selectedPencilRect = pygame.Rect(self.x, self.y, self.side, self.side)
        pygame.draw.rect(self.screen, col, selectedPencilRect, 1)
    
    # if the mouse clicks the box
    def draw_clicked(self, col, thickness):
        selectedPencilRect = pygame.Rect(self.x, self.y, self.side, self.side)
        pygame.draw.rect(self.screen, col, selectedPencilRect, thickness)

        back = self.screen.copy()
        return back

    # change the tool value in the json file
    def tool_name (self, tool):
        with open("config.json") as f:
            data = json.load(f)


        data["tool"] = tool

        with open("config.json", "w") as f:
            json.dump(data, f)

    # change the boolean value for keys in the json file
    def tool_status (self, tool):
        with open("config.json") as f:
            data = json.load(f)


        data[tool] = True

        with open("config.json", "w") as f:
            json.dump(data, f)

