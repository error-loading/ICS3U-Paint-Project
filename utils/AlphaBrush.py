import pygame

class AlphaBrush:
    def __init__(self, screen, colour, size, opacity):
        self.screen = screen
        self.colour = colour
        self.size = size
        self.omx = None
        self.omy = None
        self.opacity = opacity
    
    def draw(self, mx, my):
        r = self.colour[0]
        g = self.colour[1]
        b = self.colour[2]
        a = self.opacity

        brushHead = pygame.Surface((20,20),pygame.SRCALPHA)
        self.screen.blit(brushHead, (mx, my))

    def erase(self, mx, my):
        r = self.colour[0]
        g = self.colour[1]
        b = self.colour[2]
        a = self.opacity

        eraserHead = pygame.Surface((40,40),pygame.SRCALPHA) 
        self.screen.blit(eraserHead, (mx, my))

        

