'''
Gurjas Singh Dhillon

Ellipse.py

this file is for the fill tool. it applies the flood fill algorithm and sets a new colour to neighbouring pixels
'''

import pygame
import queue

class Fill:
    # init function, have to put these paramters in when first creating an instance of the class
    def __init__(self, screen,  colour):
        self.colour = colour
        self.visited = []    # visited array to make sure there is no duplicates, this is more for a dfs/bfs search, but the two algos are pretty similar
        self.screen = screen

    # method checks if a pixel has already been visited
    def checkedVisited(self, x, y):
        if (x, y) not in self.visited:
            return 1
        return 0

    # getting the neightbours of a node
    def getNeighbours(self, x, y):
        neighbors = []

        # nested for loop to check every direction
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                # make sure that the new values are inside the canvas, and also check if the node has been already visited

                if ( x-dx > 0 and x-dx < self.screen.get_width() and y - dy > 0 and y - dy < self.screen.get_height() ) and self.checkedVisited(x-dx, y-dy): 
                    neighbors.append((x-dx, y - dy))
                    self.visited.append((x-dx, y - dy))
            
        return neighbors

    # method where the actual filling part happens
    def fill(self, x, y):
        # using a pixelarray since mr mckenzie said its faster than a normal pixel value search
        pixelArray = pygame.PixelArray(self.screen)
        
        # if the colour at point (x, y) is the same as the fill colour, exit the function
        if self.colour == pixelArray[x, y]:
            return
        
        # creating a stack in preparation of dfs seach
        q = queue.LifoQueue()
        q.put((x, y))

        # creating a set for all the nodes needing their colours changed, using a set so that no duplicate points appear
        nodes = set()

        while not q.empty():
            # take out a point and unpack it, then check for it's neighbours
            newX,newY = q.get()
            neighbors = self.getNeighbours(newX,newY)

            # if the neighouring node is ellegible, put that node in the stack and the nodes set
            for neighboringNodes in neighbors:
                if pixelArray[neighboringNodes[0], neighboringNodes[1]] == pixelArray[x, y]:
                    q.put(neighboringNodes)
                    nodes.add(neighboringNodes)
        
        # change all the nodes to the colour
        for x, y in nodes:
            pixelArray[x, y] = self.colour

        # delete the pixelArray
        del pixelArray
        
        pygame.display.flip()