'''
Gurjas Singh Dhillon

Eyedropper.py

this file is for the eyedropper tool. gets the pixel at the mouse cursor and updates the json file
'''

import pygame
import json

class Eyedropper:
    def drop(self, x, y, screen):
        # getting the colour at pixel (x, y)
        col = screen.get_at([x, y])[:3]

        # load the json file and save it as a python dict under the variable called data
        with open("config.json") as f:
            data = json.load(f)

        # change the colour value of the python dicitonary, "data" 
        data["colour"] = str(col)

        # create a new config.json file and dump all the content into it
        with open("config.json", "w") as f:
            json.dump(data, f)            