import graphics as g
import numpy as np
import maze_class as maze

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
        self.object.draw(self.w)
        
    # Need collision detection
    def control(self, key):
        self.key = key
        # counter for every player move made
        moves = 0
        if key == "Up" and maze.check_wall != "wall":
            moves += 1
            self.object.move(0, -5)
        if key == "Down" and maze.check_wall != "wall":
            moves += 1
            self.object.move(0, 5)
        if key == "Left" and maze.check_wall != "wall":
            moves += 1
            self.object.move(-5, 0)
        if key == "Right" and maze.check_wall != "wall":
            moves += 1
            self.object.move(5, 0)