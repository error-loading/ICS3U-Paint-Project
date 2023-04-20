import pygame

# pencil class
class Pencil:
    def __init__(self, screen, colour, size):
        self.colour = colour
        self.size = size
        self.screen = screen

    def draw(self, omx, omy, mx, my):
        pygame.draw.line(self.screen, self.colour, (omx, omy), (mx, my), self.size)
    
    def erase(self, mx, my):
        pygame.draw.circle(self.screen, (0, 0, 0), (mx,my), self.size)