'''
Gurjas Singh Dhillon

Stamps.py

this class is for adding the stamp imgs to the stampMenu
'''

import pygame
import sys
import json

# change the path to root of directory 
sys.path.insert(0, "..")

from config import *

class Stamps:
    def __init__ (self, screen, x, y, side, img):
        self.screen = screen
        self.x = x
        self.y = y
        self.side = side
        self.img = img


        # load the img, and then scale it so that the width is the same as the menu and the height proportional
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (side, side / self.img.get_width() * self.img.get_height()))
        
        self.boxRect = pygame.Rect(x, y, side, side / self.img.get_width() * self.img.get_height())
        pygame.draw.rect(screen, (0, 0, 0), self.boxRect, 3)
        self.screen.blit(self.img, (x, y))

    # while mouse is colliding point with the boxRect
    def draw_hover (self, col):
        selectedPencilRect = pygame.Rect(self.x, self.y, self.side, self.side / self.img.get_width() * self.img.get_height())
        pygame.draw.rect(self.screen, col, selectedPencilRect, 3)
    
    # if the mouse clicks the box
    def draw_clicked(self, col, thickness):
        selectedPencilRect = pygame.Rect(self.x, self.y, self.side, self.side / self.img.get_width() * self.img.get_height())
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


