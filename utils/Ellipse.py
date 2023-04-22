'''
Gurjas Singh Dhillon

Ellipse.py

this file is for the ellipse tool. it draws the motion of the ellipse and also sends a permanent copy back to the mainScreen file
'''

import pygame

class Ellipse:
    def __init__(self, screen, colour, omx, omy, size):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True
        self.size = size

    # this method is called after mouse is first clicked, and this is what gives the dragging allusion
    def draw(self, mx, my):
        # checks for all cases of the mouse positions
        if mx-self.omx > 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(self.omx, self.omy, mx-self.omx, my-self.omy)
        elif mx-self.omx < 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(mx, self.omy, self.omx-mx, my-self.omy)
        elif mx-self.omx > 0 and my - self.omy < 0:
            ellipseRect = pygame.Rect(self.omx, my, mx-self.omx, self.omy-my)
        else:
            ellipseRect = pygame.Rect(mx, my, self.omx-mx, self.omy-my)

        # draw the ellipse to the screen
        pygame.draw.ellipse(self.screen, self.colour, ellipseRect, self.size)
    
    # if the mouse is up, same as above method, but returns a screenshot of the canvas
    def drawPer(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(self.omx, self.omy, mx-self.omx, my-self.omy)
        elif mx-self.omx < 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(mx, self.omy, self.omx-mx, my-self.omy)
        elif mx-self.omx > 0 and my - self.omy < 0:
            ellipseRect = pygame.Rect(self.omx, my, mx-self.omx, self.omy-my)
        else:
            ellipseRect = pygame.Rect(mx, my, self.omx-mx, self.omy-my)
        pygame.draw.ellipse(self.screen, self.colour, ellipseRect, self.size)

        # takes a screenshot and returns it back to the mainScreen.py file
        bgImg = self.screen.copy()
        return bgImg