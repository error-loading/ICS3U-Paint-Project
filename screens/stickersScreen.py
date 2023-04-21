import pygame
from config import *
from tkinter import filedialog
import tkinter as tk
import sys



# change the path to root of directory 
sys.path.insert(0, "..")

# import RectImgs class
from utils.Stamps import Stamps
from utils.RectImgs import RectImgs

# importing constants from config.py file
from config import *

pygame.init()

def collision(mx, my, x, y, w, h):
    if mx >= x and mx <= x + w and my >= y and my <= y + h:
        return True
    return False

# sticker menu
def sticker():

    occupied = [False, False, False, False, False, False]
    posImg = {
        1 : (50, 50),
        2 : (150, 50),
        3 : (250, 50), 
        4 : (350, 50),
        5 : (450, 50),
        6 : (550, 50)
    }

    screen = pygame.display.set_mode((200, 720))
    pygame.display.set_caption("Sticker Menu")


    running = True

    # test 1
    smth = Stamps(screen, 40, 40, 100, 100, "imgs/tools/1.png")
    smth.draw((0, 0, 0, 72))
    

    while running:

        screen.fill(WHITE)
        smthRect = pygame.Surface.get_rect(smth.exitedSur)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False
            

        mx, my = pygame.mouse.get_pos()
        
        if collision(mx, my, smth.x + smth.width - 20, smth.y - 20, 40, 40):
            smth.draw((0, 0, 0, 32))
        
        else:
            smth.draw((0, 0, 0, 72))

        pygame.display.flip()