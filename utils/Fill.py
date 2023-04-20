import queue
import pygame

class Fill:
    def __init__(self, screen,  colour):
        self.colour = colour
        self.visited = []
        self.screen = screen

    def checkedVisited(self, x, y):
        if (x, y) not in self.visited:
            return 1
        return 0

    def getNeighbours(self, x, y):
        neighbors = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if ( x-dx > 0 and x-dx < self.screen.get_width() and y - dy > 0 and y - dy < self.screen.get_height() ) and self.checkedVisited(x-dx, y-dy): 
                    neighbors.append((x-dx, y - dy))
                    self.visited.append((x-dx, y - dy))
            
        return neighbors

    def fill(self, x, y):
        pixelArray = pygame.PixelArray(self.screen)
        
        if self.colour == pixelArray[x, y]:
            return
        
        q = queue.LifoQueue()
        q.put((x, y))

        nodes = set()

        while not q.empty():
            newX,newY = q.get()
            neighbors = self.getNeighbours(newX,newY)

            for neighboringNodes in neighbors:
                if pixelArray[neighboringNodes[0], neighboringNodes[1]] == pixelArray[x, y]:
                    q.put(neighboringNodes)
                    nodes.add(neighboringNodes)
        
        for x, y in nodes:
            pixelArray[x, y] = self.colour

        del pixelArray
        
        pygame.display.flip()