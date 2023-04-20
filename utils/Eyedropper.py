import pygame
import json

class Eyedropper:
    def drop(self, x, y, screen):
        col = screen.get_at([x, y])[:3]

        with open("config.json") as f:
            data = json.load(f)

        open('config.json', 'w').close()

        data["colour"] = str(col)

        with open("config.json", "w") as f:
            json.dump(data, f)            