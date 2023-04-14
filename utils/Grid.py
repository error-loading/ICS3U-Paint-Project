import pygame
import sys

sys.path.insert(0,"..")

from config import *


class Grid:
    def __init__(self, screen, HEIGHT, WIDTH):
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
    def on(self, col):
        for i in range(0, self.WIDTH, 25):
            pygame.draw.line(self.screen, col, (i, -10), (i, self.HEIGHT + 10), 1)
        for i in range(0, self.HEIGHT, 25):
            pygame.draw.line(self.screen, col, (-10, i), (self.WIDTH + 10, i), 1)
    def off(self):
        for i in range(0, self.WIDTH, 25):
            pygame.draw.line(self.screen, WHITE, (i, -10), (i, self.HEIGHT + 10), 1)
        for i in range(0, self.HEIGHT, 25):
            pygame.draw.line(self.screen, WHITE, (-10, i), (self.WIDTH + 10, i), 1)