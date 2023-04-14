import pygame

class Eyedropper:
    def __init__(self, x, y, screen):
        return screen.get_at([x, y])[:3]