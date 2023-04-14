import pygame

class Paintbrush:
  def __init__(self, size, colour, bgCol, state, screen):
    self.size = size
    self.colour = colour
    self.bgCol = bgCol
    self.prevCoor = (-1, -1)
    self.state = state
  def draw(self, mx, my):
    # if it is a new stroke
    if self.state == 0:
        pygame.draw.circle(self.screen, self.colour, (mx, my), self.size)
        self.prevCoor = (mx, my)
        self.state = 1
    
    # part of prev stroke
    elif self.state == 1:
        deltaX = self.prevCoor[0] - mx
        deltaY = self.prevCoor[1] - my
        dist = (deltaX**2 + deltaY**2)**0.5
        dist = max(deltaX, deltaY)

        for d in range(int(dist)):
            if not dist:
                break
            cenX = self.prevCoor[0] + d/dist * (self.prevCoor[0] - mx)
            cenY = self.prevCoor[1] + d/dist * (self.prevCoor[1] - my)
            pygame.draw.circle(self.screen, self.colour, (cenX, cenY), self.size)
        
        self.prevCoor = (mx, my)
    