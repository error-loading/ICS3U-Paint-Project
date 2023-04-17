import queue
import pygame

class Fill:
    def __init__(self, screen,  colour, colourClicked):
        self.colour = colour
        self.colourClicked = colourClicked
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
        if self.colour == self.colourClicked:
            return
        
        q = queue.LifoQueue()
        q.put((x, y))

        while not q.empty():
            newX,newY = q.get()
            neighbors = self.getNeighbours(newX,newY)

            for neighboringNodes in neighbors:
                if self.screen.get_at([neighboringNodes[0], neighboringNodes[1]])[:3] == self.colourClicked:
                    self.screen.set_at(neighboringNodes, self.colour)
                    q.put(neighboringNodes)
        pygame.display.flip()