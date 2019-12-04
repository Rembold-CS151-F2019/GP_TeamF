import graphics as g
import numpy as np

class Player:
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
        self.draw()
        
    # Maybe do some sort of nicer graphic for the player eventually??
    def draw(self):
        self.object = g.Circle(g.Point(self.x, self.y), 20)
        self.object.setFill("red")
        self.object.draw(w)
        
    # Need collision detection
    def control(self, key):
        self.key = key
        # counter for every player move made
        moves = 0
        if key == "Up":
            moves += 1
            self.object.move(0, -5)
        if key == "Down":
            moves += 1
            self.object.move(0, 5)
        if key == "Left":
            moves += 1
            self.object.move(-5, 0)
        if key == "Right":
            moves += 1
            self.object.move(5, 0)