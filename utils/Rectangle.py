import pygame

class Rectangle:
    def __init__(self, screen, colour, omx, omy, size):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True
        self.size = size

    def draw(self, mx, my):
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

        bgImg = self.screen.copy()
        return bgImg