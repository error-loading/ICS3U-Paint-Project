'''
Gurjas Singh Dhillon

Lines.py

this file is for the Lines tool. it has the same logic as the other shapes
'''

import pygame

class Line:
    def __init__(self, screen, colour, omx, omy, size):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True
        self.size = size

    def draw(self, mx, my):
        pygame.draw.line(self.screen, self.colour, (self.omx, self.omy), (mx, my), self.size)
    
    # if the mouse is up
    def drawPer(self, mx, my):
        pygame.draw.line(self.screen, self.colour, (self.omx, self.omy), (mx, my), self.size)

        bgImg = self.screen.copy()
        return bgImg