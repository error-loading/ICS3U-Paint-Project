'''
Gurjas Singh Dhillon

Rectangle.py

this file is for the rectangle tool. same logic as the other shape tools
'''

import pygame

class Rectangle:
    def __init__(self, screen, colour, omx, omy, size):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True
        self.size = size

    # while mouse is held down
    def draw(self, mx, my):
        # check through all combinations of the mouse
        if mx-self.omx > 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, self.omy, mx-self.omx, my-self.omy), self.size)

        elif mx-self.omx < 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (mx, self.omy, self.omx-mx, my-self.omy), self.size)

        elif mx-self.omx > 0 and my - self.omy < 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, my, mx-self.omx, self.omy-my), self.size)

        else:
            pygame.draw.rect(self.screen, self.colour, (mx, my, self.omx-mx, self.omy-my), self.size)
    
    # if the mouse is up
    def drawPer(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, self.omy, mx-self.omx, my-self.omy), self.size)
        elif mx-self.omx < 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (mx, self.omy, self.omx-mx, my-self.omy), self.size)
        elif mx-self.omx > 0 and my - self.omy < 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, my, mx-self.omx, self.omy-my), self.size)
        else:
            pygame.draw.rect(self.screen, self.colour, (mx, my, self.omx-mx, self.omy-my), self.size)

        # take a screenshot and return it so that the mainscreen can append it to the undo list
        bgImg = self.screen.copy()
        return bgImg