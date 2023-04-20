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
        pygame.draw.rect(surface, (200, 200, 200), (self.x, self.y, self.width, self.height))
        handle_pos = max(self.x, min(self.x + self.width * self.value - self.height/2, self.x + self.width - self.height))
        pygame.draw.rect(surface, (100, 100, 100), (handle_pos, self.y, self.height, self.height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
            
            with open("config.json") as f:
                data = json.load(f)
            
            open("config.json").close()

            data["size"] = int(self.value * 50)

            with open("config.json", "w") as f:
                json.dump(data, f)


        if event.type == pygame.MOUSEMOTION and self.dragging:
            pos = pygame.mouse.get_pos()
            self.value = min(1.0, max(0.0, (pos[0] - self.x) / self.width))

    def get_value(self):
        return self.value