import pygame

class Line:
    def __init__(self, screen, colour, omx, omy):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True

    def draw(self, mx, my):
        pygame.draw.line(self.screen, self.colour, (self.omx, self.omy), (mx, my))
    
    # if the mouse is up
    def drawPer(self, mx, my):
        pygame.draw.line(self.screen, self.colour, (self.omx, self.omy), (mx, my))

        bgImg = self.screen.copy()
        return bgImg