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

        

