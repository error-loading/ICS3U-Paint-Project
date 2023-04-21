from tkinter import *
from tkinter import filedialog
import pygame

Tk().withdraw() #hides the small extra window

class Load:
    def __init__(self, screen):
        self.screen = screen
        
    def ask(self):
        fname = filedialog.askopenfilename()
        if fname == "":
            return False

        return fname

    

