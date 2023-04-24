'''
Gurjas Singh Dhillon

Slider.py

this file is for the slider that decides the thickness of every tool
'''

# import libraries
import pygame
import json
import sys

# change the path to root of directory 
sys.path.insert(0, "..")

class Slider:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = 0.0  
        self.dragging = False  

    def draw(self, surface):
        # background rectangle of the slider
        pygame.draw.rect(surface, (200, 200, 200), (self.x, self.y, self.width, self.height))

        # handle of the slider
        handle_pos = max(self.x, min(self.x + self.width * self.value - self.height/2, self.x + self.width - self.height))
        pygame.draw.rect(surface, (100, 100, 100), (handle_pos, self.y, self.height, self.height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            if self.x <= mx <= self.x + self.width and self.y <= my <= self.y + self.height:
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
            
            with open("config.json") as f:
                data = json.load(f)


            data["size"] = int(self.value * 50)

            with open("config.json", "w") as f:
                json.dump(data, f)


        if event.type == pygame.MOUSEMOTION and self.dragging:
            mx, my = pygame.mouse.get_pos()
            self.value = min(1, max(0, (mx - self.x) / self.width))

    def get_value(self):
        return self.value