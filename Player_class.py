import graphics as g
#import numpy as np
# Importing Isa's class to use
import maze_class as m
#import Control as k

class Player:
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
        self.draw()
        
    # Making the visual representation of the player
    def draw(self):
        self.object = g.Circle(g.Point(self.x, self.y), 20)
        self.object.setFill("DarkViolet")
        self.object.draw(w)
        
    # Allows for keyboard control and does not allow moves if wall is present
    def control(self, key):
        self.key = key
        # counter for every player move made
        moves = 0
        # Allows for either arrows or WASD movement
        if key == "Up" and m.Maze.check_wall != "wall" or key == "w" and m.Maze.check_wall() != "wall":
            moves += 1
            self.object.move(0, -20)
        if key == "Down" and m.Maze.check_wall != "wall" or key == "s" and m.Maze.check_wall() != "wall":
            moves += 1
            self.object.move(0, 20)
        if key == "Left" and m.Maze.check_wall != "wall" or key == "a" and m.Maze.check_wall() != "wall":
            moves += 1
            self.object.move(-20, 0)
        if key == "Right" and m.Maze.check_wall != "wall" or key == "d" and m.Maze.check_wall() != "wall":
            moves += 1
            self.object.move(20, 0)