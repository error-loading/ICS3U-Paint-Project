import pygame

class Ellipse:
    def __init__(self, screen, colour, omx, omy):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.colour = colour
        self.firstClicked = True

    def draw(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(self.omx, self.omy, mx-self.omx, my-self.omy)
        elif mx-self.omx < 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(mx, self.omy, self.omx-mx, my-self.omy)
        elif mx-self.omx > 0 and my - self.omy < 0:
            ellipseRect = pygame.Rect(self.omx, my, mx-self.omx, self.omy-my)
        else:
            ellipseRect = pygame.Rect(mx, my, self.omx-mx, self.omy-my)
        pygame.draw.ellipse(self.screen, self.colour, ellipseRect, 1)
    
    # if the mouse is up
    def drawPer(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(self.omx, self.omy, mx-self.omx, my-self.omy)
        elif mx-self.omx < 0 and my - self.omy > 0:
            ellipseRect = pygame.Rect(mx, self.omy, self.omx-mx, my-self.omy)
        elif mx-self.omx > 0 and my - self.omy < 0:
            ellipseRect = pygame.Rect(self.omx, my, mx-self.omx, self.omy-my)
        else:
            ellipseRect = pygame.Rect(mx, my, self.omx-mx, self.omy-my)
        pygame.draw.ellipse(self.screen, self.colour, ellipseRect, 1)

        bgImg = self.screen.copy()
        return bgImg