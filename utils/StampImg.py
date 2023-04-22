'''
Gurjas Singh Dhillon

StampImg.py

this class is for placing the stamps on the mainscreen. same logic as the rectangle tool
'''

import pygame

class StampImg:
    def __init__(self, screen, omx, omy, img):
        self.screen = screen
        self.omx = omx
        self.omy = omy
        self.firstClicked = True
        self.img = pygame.image.load(img)

    # mouse in motion
    def draw(self, mx, my):
        # trying all combinations
        if mx-self.omx > 0 and my - self.omy > 0:
            newImg = pygame.transform.scale(self.img, (abs(mx-self.omx), abs(my-self.omy)))
            self.screen.blit(newImg, (self.omx, self.omy))

        elif mx-self.omx < 0 and my - self.omy > 0:
            newImg = pygame.transform.scale(self.img, (abs(self.omx-mx), abs(my-self.omy)))
            self.screen.blit(newImg, (mx, self.omy))

        elif mx-self.omx > 0 and my - self.omy < 0:
            newImg = pygame.transform.scale(self.img, (abs(mx-self.omx), abs(self.omy-my)))
            self.screen.blit(newImg, (self.omx, my))

        else:
            newImg = pygame.transform.scale(self.img, (abs(self.omx-mx), abs(self.omy-my)))
            self.screen.blit(newImg, (mx, my))

    
    # if the mouse is up, last time this instance of the mouse is drawn, it later sends back a screenshot which is appended to the undo list
    def drawPer(self, mx, my):
        if mx-self.omx > 0 and my - self.omy > 0:
            newImg = pygame.transform.scale(self.img, (abs(mx-self.omx), abs(my-self.omy)))
            self.screen.blit(newImg, (self.omx, self.omy))

        elif mx-self.omx < 0 and my - self.omy > 0:
            newImg = pygame.transform.scale(self.img, (abs(self.omx-mx), abs(my-self.omy)))
            self.screen.blit(newImg, (mx, self.omy))

        elif mx-self.omx > 0 and my - self.omy < 0:
            newImg = pygame.transform.scale(self.img, (abs(mx-self.omx), abs(self.omy-my)))
            self.screen.blit(newImg, (self.omx, my))

        else:
            newImg = pygame.transform.scale(self.img, (abs(self.omx-mx), abs(self.omy-my)))
            self.screen.blit(newImg, (mx, my))

        bgImg = self.screen.copy()
        return bgImg