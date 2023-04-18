from tkinter import *
from tkinter import filedialog
import pygame

Tk().withdraw() #hides the small extra window

class Save:
    def __init__(self, screen):
        self.screen = screen
        
    def ask(self):
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        bgImg = self.screen.copy()

        pygame.image.save(bgImg, fname)

