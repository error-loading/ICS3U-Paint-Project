import pygame
import queue

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running =True

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
                if x-dx > 0 and x-dx < WIDTH and y - dy > 0 and y - dy < HEIGHT and self.checkedVisited(x-dx, y-dy): 
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

FillTool = Fill((0, 0, 0), (255, 255, 255))



screen.fill((255, 255, 255))
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    # ----------------------------------
    # Your code goes here.
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()
    pygame.draw.line(screen, (0, 0, 0), (25, 25), (50, 25))
    pygame.draw.line(screen, (0, 0, 0), (25, 25), (25, 50))
    pygame.draw.line(screen, (0, 0, 0), (25, 50), (50, 50))
    pygame.draw.line(screen, (0, 0, 0), (50, 50), (50, 25))

    pygame.draw.line(screen, (0, 0, 0), (25, 100), (50, 100))
    pygame.draw.line(screen, (0, 0, 0), (25, 100), (25, 150))
    pygame.draw.line(screen, (0, 0, 0), (25, 150), (50, 150))
    pygame.draw.line(screen, (0, 0, 0), (50, 150), (50, 100))
    if mb[0]:
        FillTool.fill(mx, my)
    # ----------------------------------
    pygame.display.flip()

pygame.quit()