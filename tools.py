import pygame
import queue

WIDTH = 800
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH,HEIGHT))

running =True

tool = "polygon"
polygonFirst = True

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class Fill:
    def __init__(self, colour, colourClicked):
        self.colour = colour
        self.colourClicked = colourClicked
        self.visited = []

    def checkedVisited(self, x, y):
        if (x, y) not in self.visited:
            return 1
        return 0

    def getNeighbours(self, x, y):
        neighbors = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if ( x-dx > 0 and x-dx < WIDTH and y - dy > 0 and y - dy < HEIGHT ) and self.checkedVisited(x-dx, y-dy): 
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
                if screen.get_at([neighboringNodes[0], neighboringNodes[1]])[:3] == self.colourClicked:
                    screen.set_at(neighboringNodes, self.colour)
                    q.put(neighboringNodes)
        pygame.display.flip()


class Polygon:
    def __init__(self):
        self.points = []
        self.startCoor = ()
        self.prevCoor = ()
    
    def firstCircle(self, x, y):
        self.startCoor = (x, y)
        self.prevCoor = (x, y)
        pygame.draw.circle(screen, GREEN, (x, y), 6)
    
    def nextCircle(self, x, y, size, colour):

        pygame.draw.line(screen, BLACK, self.prevCoor, (x, y), size)
        pygame.draw.circle(screen, BLACK, self.prevCoor, 6)
        pygame.draw.circle(screen, RED, (x, y), 6)

        if self.prevCoor == self.startCoor:
            pygame.draw.circle(screen, GREEN, self.startCoor, 6)
        
        self.prevCoor = (x, y)
    
    def endCircle(self, colour):

        pygame.draw.line(screen, BLACK, self.prevCoor, self.startCoor, 6)
        pygame.draw.circle(screen, (0, 0, 0), self.prevCoor, 6)
        pygame.draw.circle(screen, (0, 0, 0), self.startCoor, 6)



class Eyedropper:
    def __init__(self, x, y):
        return screen.get_at([x, y])[:3]



FillTool = Fill((0, 0, 0), (255, 255, 255))




cnt = 0

screen.fill((255, 255, 255))
while running:
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        
        if evt.type == pygame.MOUSEBUTTONDOWN:
            if tool == "polygon":
                if polygonFirst:
                    poly = Polygon()
                    poly.firstCircle(mx, my)
                    polygonFirst = False
                elif poly.startCoor[0] - 6 <= mx and poly.startCoor[0] + 6 >= mx and poly.startCoor[1] - 6 <= my and poly.startCoor[1] + 6 >= my:
                    poly.endCircle((0, 0, 0))
                    polygonFirst = True
                    continue
                else:
                    poly.nextCircle(mx, my, 6, (0, 0, 0))
            
            if tool == "fill":
                FillTool.fill(mx, my)

    # ----------------------------------
    # Your code goes here.

    pygame.draw.line(screen, (0, 0, 0), (25, 25), (50, 25))
    pygame.draw.line(screen, (0, 0, 0), (25, 25), (25, 50))
    pygame.draw.line(screen, (0, 0, 0), (25, 50), (50, 50))
    pygame.draw.line(screen, (0, 0, 0), (50, 50), (50, 25))

    pygame.draw.line(screen, (0, 0, 0), (25, 100), (50, 100))
    pygame.draw.line(screen, (0, 0, 0), (25, 100), (25, 150))
    pygame.draw.line(screen, (0, 0, 0), (25, 150), (150, 150))
    pygame.draw.line(screen, (0, 0, 0), (150, 150), (50, 100), 4)
    # ----------------------------------
    pygame.display.flip()

pygame.quit()