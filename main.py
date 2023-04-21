'''
main.py
Gurjas Dhillon
this program launches all the processes. it starts the three separate windows using a library called multiprocess
'''

# import libraries
import pygame 
import multiprocessing
import queue
import os

# import local files
from screens.mainScreen import mainScreen 
from screens.toolbar import toolbarScreen
from screens.stickersScreen import sticker


if __name__ == "__main__": # setup area for processes
    # makes and starts all the processes of the different windows
    toolbarScreenP = multiprocessing.Process(target=toolbarScreen) # toolbar processes
    mainScreenP = multiprocessing.Process(target=mainScreen) # main canvas proccess
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