import pygame
import queue

WIDTH = 800
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen2 = pygame.display.set_mode((WIDTH,HEIGHT))

running =True

tool = "pb"
polygonFirst = True
pbDrew = False

omx, omy = 0, 0

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pics = []

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

class Grid:
    def on(self, col):
        for i in range(0, WIDTH, 25):
            pygame.draw.line(screen, col, (i, -10), (i, HEIGHT + 10), 1)
        for i in range(0, HEIGHT, 25):
            pygame.draw.line(screen, col, (-10, i), (WIDTH + 10, i), 1)
    def off(self):
        for i in range(0, WIDTH, 25):
            pygame.draw.line(screen, WHITE, (i, -10), (i, HEIGHT + 10), 1)
        for i in range(0, HEIGHT, 25):
            pygame.draw.line(screen, WHITE, (-10, i), (WIDTH + 10, i), 1)

class Paintbrush:
  def __init__(self, size, colour, bgCol, state):
    self.size = size
    self.colour = colour
    self.bgCol = bgCol
    self.prevCoor = (-1, -1)
    self.state = state
  def draw(self, mx, my):
    # if it is a new stroke
    if self.state == 0:
        pygame.draw.circle(screen, self.colour, (mx, my), self.size)
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
            pygame.draw.circle(screen, self.colour, (cenX, cenY), self.size)
        
        self.prevCoor = (mx, my)
    

 

FillTool = Fill((0, 0, 0), (255, 255, 255))
grid = Grid()
pb = Paintbrush(5, BLACK, WHITE, 0)




cnt = 0

screen.fill((255, 255, 255))
while running:

    if len(pics) > 0:
        screen.blit(pics[-1], (0, 0))

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
            if tool == "grid":
                grid.off()
            

        
        if evt.type == pygame.MOUSEBUTTONUP:
            if tool == "rect" and omx and omy:
                if mx-omx > 0 and my - omy > 0:
                    x = pygame.draw.rect(screen, BLACK, (omx, omy, mx-omx, my-omy), 1)
                elif mx-omx < 0 and my - omy > 0:
                    x = pygame.draw.rect(screen, BLACK, (mx, omy, omx-mx, my-omy), 1)
                elif mx-omx > 0 and my - omy < 0:
                    x = pygame.draw.rect(screen, BLACK, (omx, my, mx-omx, omy-my), 1)
                else:
                    x = pygame.draw.rect(screen, BLACK, (mx, my, omx-mx, omy-my), 1)
                back = screen.copy()
                pics.append(back)
                omx, omy = 0, 0
            if tool == "pb":
                pb.state = 0
                pb.prevCoor = (-1, -1)
                pbDrew = False

    if pbDrew:
        pb.draw(mx, my)

    if mb[0]:

        if tool == "pb":
            pbDrew = True

        if not omx and not omy:
            omx, omy = mx, my
        
        elif tool == "rect" and omx and omy:
            if mx-omx > 0 and my - omy > 0:
                pygame.draw.rect(screen, BLACK, (omx, omy, mx-omx, my-omy), 1)
            elif mx-omx < 0 and my - omy > 0:
                pygame.draw.rect(screen, BLACK, (mx, omy, omx-mx, my-omy), 1)
            elif mx-omx > 0 and my - omy < 0:
                pygame.draw.rect(screen, BLACK, (omx, my, mx-omx, omy-my), 1)
            else:
                pygame.draw.rect(screen, BLACK, (mx, my, omx-mx, omy-my), 1)

    pygame.display.flip()
