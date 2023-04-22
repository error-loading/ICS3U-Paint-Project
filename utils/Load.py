'''
Gurjas Singh Dhillon

Load.py

this file is for the load tool. it opens a dialog box using tkinter and gets the user to enter a filename, then this class returns the path to the file
'''

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

    