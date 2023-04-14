import pygame

from ..config import *

class Polygon:
    def __init__(self, screen):
        self.points = []
        self.startCoor = ()
        self.prevCoor = ()
    
    def firstCircle(self, x, y):
        self.startCoor = (x, y)
        self.prevCoor = (x, y)
        pygame.draw.circle(self.screen, GREEN, (x, y), 6)
    
    def nextCircle(self, x, y, size, colour):

        pygame.draw.line(self.screen, BLACK, self.prevCoor, (x, y), size)
        pygame.draw.circle(self.screen, BLACK, self.prevCoor, 6)
        pygame.draw.circle(self.screen, RED, (x, y), 6)

        if self.prevCoor == self.startCoor:
            pygame.draw.circle(self.screen, GREEN, self.startCoor, 6)
        
        self.prevCoor = (x, y)
    
    def endCircle(self, colour):

        pygame.draw.line(self.screen, BLACK, self.prevCoor, self.startCoor, 6)
        pygame.draw.circle(self.screen, (0, 0, 0), self.prevCoor, 6)
        pygame.draw.circle(self.screen, (0, 0, 0), self.startCoor, 6)