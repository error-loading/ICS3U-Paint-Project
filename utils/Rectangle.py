import pygame

class Rectangle:
    def __init__(self, screen, colour, omx, omy):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True

    def draw(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, self.omy, mx-self.omx, my-self.omy), 1)
        elif mx-self.omx < 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (mx, self.omy, self.omx-mx, my-self.omy), 1)
        elif mx-self.omx > 0 and my - self.omy < 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, my, mx-self.omx, self.omy-my), 1)
        else:
            pygame.draw.rect(self.screen, self.colour, (mx, my, self.omx-mx, self.omy-my), 1)
    
    # if the mouse is up
    def drawPer(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, self.omy, mx-self.omx, my-self.omy), 1)
        elif mx-self.omx < 0 and my - self.omy > 0:
            pygame.draw.rect(self.screen, self.colour, (mx, self.omy, self.omx-mx, my-self.omy), 1)
        elif mx-self.omx > 0 and my - self.omy < 0:
            pygame.draw.rect(self.screen, self.colour, (self.omx, my, mx-self.omx, self.omy-my), 1)
        else:
            pygame.draw.rect(self.screen, self.colour, (mx, my, self.omx-mx, self.omy-my), 1)

        bgImg = self.screen.copy()
        return bgImg