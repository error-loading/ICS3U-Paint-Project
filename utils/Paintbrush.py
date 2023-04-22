'''
Gurjas Singh Dhillon

Paintbrush.py

this file is for the paintbrush tool. it gets mouse's old position and the mouses new position and draws circle in between them using similar triangles and math
'''

import pygame

class Paintbrush:
  def __init__(self, screen,size, colour, bgCol, state):
    self.size = size // 2
    self.colour = colour
    self.bgCol = bgCol
    self.prevCoor = (-1, -1)
    self.state = state
    self.screen = screen

  def draw(self, mx, my):
    # if it is a new stroke
    if self.state == 0:
        pygame.draw.circle(self.screen, self.colour, (mx, my), self.size)
        self.prevCoor = (mx, my)
        self.state = 1  # make sure next time the program knows that this is alr part of a stroke
    
    # part of prev stroke
    elif self.state == 1:
        # calculate the distance between the points
        deltaX = self.prevCoor[0] - mx
        deltaY = self.prevCoor[1] - my
        dist = (deltaX**2 + deltaY**2)**0.5

        # draw circle in between them
        for d in range(int(dist)):
            if not dist:
                break
            cenX = self.prevCoor[0] + d/dist * (mx-self.prevCoor[0])
            cenY = self.prevCoor[1] + d/dist * (my-self.prevCoor[1])
            pygame.draw.circle(self.screen, self.colour, (cenX, cenY), self.size)
        
        self.prevCoor = (mx, my)
        
  # erase
  def erase(self, mx, my):
      pygame.draw.circle(self.screen, self.bgCol, (mx,my),self.size)
    