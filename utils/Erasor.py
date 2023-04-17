import pygame

class Erasor:
    def __init__(self, screen, size, bgCol):
        self.screen = screen
        self.size = size//2
        self.bgCol = bgCol
    
    def erase(self, mx, my):
        pygame.draw.circle(self.screen, self.bgCol, (mx, my), self.size)
