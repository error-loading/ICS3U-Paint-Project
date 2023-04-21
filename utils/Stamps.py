import pygame
import sys
import json

# change the path to root of directory 
sys.path.insert(0, "..")

from config import *

class Stamps:
    def __init__ (self, screen, x, y, width, height, img):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(img)
        

    def draw (self, col):
        self.boxRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (0, 0, 0), self.boxRect, 1)

        self.img = pygame.transform.scale(self.img, (self.width - 10, self.height - 10))


        self.screen.blit(self.img, (self.x+5, self.y+5))

        self.exitedSur = self.exited(col)


        self.screen.blit(self.exitedSur, (self.x + self.width - 20, self.y - 20))


    def exited(self, col):
        exitedSur = pygame.Surface((40, 40), pygame.SRCALPHA)

        pygame.draw.circle(exitedSur, col, (20, 20), 20)


        pygame.draw.line(exitedSur, WHITE, (10, 10), (30, 30), 3)
        pygame.draw.line(exitedSur, WHITE, (10, 30), (30, 10), 3)

        self.exitedSur = exitedSur

        return exitedSur

