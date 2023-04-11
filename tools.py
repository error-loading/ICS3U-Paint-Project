import pygame
import queue

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running =True

class Fill:
    def __init__(self, colour, colourClicked, clickedX, clickedY):
        self.colour = colour
        self.colourClicked = colourClicked
        self.clickedX = clickedX
        self.clickedY = clickedY

    def getNeighbours(self, x, y):
        neighbors = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if x-dx != 0 or x-dx != WIDTH or y - dy != 0 or y - dy != HEIGHT: neighbors.append((x-dx, y - dy))
            
        return neighbors

    def fill(self):
        if self.colour == self.colourClicked:
            return
        
        q = queue.Queue()
        q.put((self.clickedX, self.clickedY))

        while q:
            newX,newY = q.pop()
            neighbors = self.generateNeighbors(newX,newY)

            for neighboringNodes in neighbors:
                #checks if the neighbor hasn't been visited (isn't the same colour of the pixel that was picked pixel)
                if screen.get_at([neighboringNodes[0], neighboringNodes[1]])[:3] == self.colourClickedAt:
                    screen.set_at((neighboringNodes[0],neighboringNodes[1]), self.colour)
                    q.put(neighboringNodes)



while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    # ----------------------------------
    # Your code goes here.

    
    # ----------------------------------
    pygame.display.flip()

pygame.quit()