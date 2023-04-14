import pygame
from config import *

pygame.init()

# sticker menu
def sticker():

    screen = pygame.display.set_mode((200, 720))
    pygame.display.set_caption("Sticker Menu")


    running = True
    
    offset = 0 # scrolling offset from starting position

    notClickedRectangle = pygame.Surface((10, 240), pygame.SRCALPHA) # scrollbar thumb (not clicked)
    pygame.draw.rect(notClickedRectangle, (255, 255, 255, 122), (0, 0, 10, 240))

    while running:
        justPressed = False
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()