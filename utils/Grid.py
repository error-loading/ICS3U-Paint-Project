import pygame
import sys

sys.path.insert(0,"..")

from config import *


class Grid:
    def __init__(self, screen, HEIGHT, WIDTH, col):
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.col = (100,100,100)
    def on(self):
        for i in range(25, self.WIDTH, 25):
            verticalLineHead = pygame.Surface((1, self.HEIGHT), pygame.SRCALPHA)
            verticalLineHead.fill((self.col[0], self.col[1], self.col[2], 10))
            self.screen.blit(verticalLineHead, (i, 0))

        for i in range(25, self.HEIGHT, 25):
            horizontalLineHead = pygame.Surface((self.WIDTH, 1), pygame.SRCALPHA)
            horizontalLineHead.fill((self.col[0], self.col[1], self.col[2], 10))
            self.screen.blit(horizontalLineHead, (0, i))

    def off(self):
        for i in range(0, self.WIDTH, 25):
            pygame.draw.line(self.screen, WHITE, (i, -10), (i, self.HEIGHT + 10), 1)
        for i in range(0, self.HEIGHT, 25):
            pygame.draw.line(self.screen, WHITE, (-10, i), (self.WIDTH + 10, i), 1)