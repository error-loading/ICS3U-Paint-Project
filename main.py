'''
main.py
Gurjas Dhillon

'''

# import libraries
import pygame 
import multiprocessing
import queue
import os
import tkinter
import json

# import local files
from screens.mainScreen import mainScreen 
from screens.toolbar import toolbarScreen
from screens.stickersScreen import sticker

with open("config.json") as json_file:
    data = json.load(json_file)

if __name__ == "__main__": # setup area for processes
   

    # makes and starts all the processes of the different windows
    mainScreenP = multiprocessing.Process(target=mainScreen, arg=(data["tool"], data["colour"], data["size"], data["opacity"])) # main canvas proccess
    toolbarScreenP = multiprocessing.Process(target=toolbarScreen) # toolbar processes
    stickerP = multiprocessing.Process(target=sticker) # sticker menu process
    mainScreenP.start()
    toolbarScreenP.start()
    stickerP.start()

    # constantly checks if anyone of the windows has been closed and closes all windows and current program
    while True:
        if not mainScreenP.is_alive() or not toolbarScreenP.is_alive() or not stickerP.is_alive():
            mainScreenP.terminate()
            toolbarScreenP.terminate()
            stickerP.terminate()
            break