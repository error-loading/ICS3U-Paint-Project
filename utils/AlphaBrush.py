import pygame


# class for brush with adjustable alpha value
class AlphaBrush:
    def __init__(self, screen, colour, colourErase , size, opacity):
        self.screen = screen
        self.colour = colour
        self.size = size
        self.omx = None
        self.omy = None
        self.opacity = opacity
        self.colourErase = colourErase

    
    def draw(self, mx, my):
        brushHead = pygame.Surface((self.size,self.size),pygame.SRCALPHA)       
        pygame.draw.circle(brushHead,self.colour,(self.size//2,self.size//2),self.size//2)

        self.screen.blit(brushHead, (mx, my))

    def erase(self, mx, my):
        eraserHead = pygame.Surface((40,40),pygame.SRCALPHA) 
        self.screen.blit(eraserHead, (mx, my))

        eraserHead = pygame.Surface((self.size,self.size),pygame.SRCALPHA)       
        pygame.draw.circle(eraserHead, self.colourErase, (self.size//2,self.size//2),self.size//2)

        self.screen.blit(eraserHead, (mx, my))

        


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
        self.state = 1
    
    # part of prev stroke
    elif self.state == 1:
        deltaX = self.prevCoor[0] - mx
        deltaY = self.prevCoor[1] - my
        dist = (deltaX**2 + deltaY**2)**0.5

        for d in range(int(dist)):
            if not dist:
                break
            cenX = self.prevCoor[0] + d/dist * (mx-self.prevCoor[0])
            cenY = self.prevCoor[1] + d/dist * (my-self.prevCoor[1])
            pygame.draw.circle(self.screen, self.colour, (cenX, cenY), self.size)
        
        self.prevCoor = (mx, my)
    
  def erase(self, mx, my):
      eraserHead = pygame.Surface((self.size,self.size),pygame.SRCALPHA)       
      pygame.draw.circle(self.screen, self.bgCol, (self.size,self.size),self.size)

      self.screen.blit(eraserHead, (mx, my))
    