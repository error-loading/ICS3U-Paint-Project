import pygame


# class for brush with adjustable alpha value
class AlphaBrush:
    def __init__(self, screen, colour, colourErase , size, state):
        self.screen = screen
        self.colour = colour
        self.size = size 
        self.omx = None
        self.omy = None
        self.bgCol = colourErase
        self.state = state


    
    def draw(self, mx, my):
        brushHead = pygame.Surface((self.size,self.size),pygame.SRCALPHA)       
        pygame.draw.circle(brushHead,tuple(list(self.colour) + [14]),(self.size / 2,self.size / 2),self.size / 2)
        self.screen.blit(brushHead, (mx, my))

    def erase(self, mx, my):

        eraserHead = pygame.Surface((self.size * 2,self.size * 2), pygame.SRCALPHA)                  
        pygame.draw.circle(eraserHead,tuple(list(self.bgCol) + [22]),(self.size,self.size),self.size)    

        self.screen.blit(eraserHead, (mx, my))
