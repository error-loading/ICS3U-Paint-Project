import pygame
import sys
import json

# change the path to root of directory 
sys.path.insert(0, "..")

from config import *

import pygame
import sys
import json

# change the path to root of directory 
sys.path.insert(0, "..")

class Stamps:
    def __init__ (self, screen, x, y, side, img):
        self.screen = screen
        self.x = x
        self.y = y
        self.side = side
        self.img = img

        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (side, side / self.img.get_width() * self.img.get_height()))
        
        self.boxRect = pygame.Rect(x, y, side, side / self.img.get_width() * self.img.get_height())
        pygame.draw.rect(screen, (0, 0, 0), self.boxRect, 3)
        self.screen.blit(self.img, (x, y))

    def draw_hover (self, col):
        selectedPencilRect = pygame.Rect(self.x, self.y, self.side, self.side / self.img.get_width() * self.img.get_height())
        pygame.draw.rect(self.screen, col, selectedPencilRect, 3)
    
    def draw_clicked(self, col, thickness):
        selectedPencilRect = pygame.Rect(self.x, self.y, self.side, self.side / self.img.get_width() * self.img.get_height())
        pygame.draw.rect(self.screen, col, selectedPencilRect, thickness)

        back = self.screen.copy()
        return back

    def tool_name (self, tool):
        with open("config.json") as f:
            data = json.load(f)

        open('config.json', 'w').close()

        data["tool"] = tool

        with open("config.json", "w") as f:
            json.dump(data, f)

    def tool_status (self, tool):
        with open("config.json") as f:
            data = json.load(f)

        open('config.json', 'w').close()

        data[tool] = True

        with open("config.json", "w") as f:
            json.dump(data, f)




# class Stamps:
#     def __init__ (self, screen, x, y, width, height, img):
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.img = pygame.image.load(img)
        

#     def draw (self, col):
#         self.boxRect = pygame.Rect(self.x, self.y, self.width, self.height)
#         pygame.draw.rect(self.screen, (0, 0, 0), self.boxRect, 1)

#         self.img = pygame.transform.scale(self.img, (self.width - 10, self.height - 10))


#         self.screen.blit(self.img, (self.x+5, self.y+5))

#         self.exitedSur = self.exited(col)


#         self.screen.blit(self.exitedSur, (self.x + self.width - 20, self.y - 20))


#     def exited(self, col):
#         exitedSur = pygame.Surface((40, 40), pygame.SRCALPHA)

#         pygame.draw.circle(exitedSur, col, (20, 20), 20)


#         pygame.draw.line(exitedSur, WHITE, (10, 10), (30, 30), 3)
#         pygame.draw.line(exitedSur, WHITE, (10, 30), (30, 10), 3)

#         self.exitedSur = exitedSur

#         return exitedSur

