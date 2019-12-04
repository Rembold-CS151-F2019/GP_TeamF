import graphics as g
import numpy as np
import maze_class as m

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
        if key == "Up" and m.Maze.check_wall != "wall" or key == "w" and m.Maze.check_wall != "wall":
            moves += 1
            self.object.move(0, -5)
        if key == "Down" and m.Maze.check_wall != "wall" or key == "s" and m.Maze.check_wall != "wall":
            moves += 1
            self.object.move(0, 5)
        if key == "Left" and m.Maze.check_wall != "wall" or key == "a" and m.Maze.check_wall != "wall":
            moves += 1
            self.object.move(-5, 0)
        if key == "Right" and m.Maze.check_wall != "wall" or key == "d" and m.Maze.check_wall != "wall":
            moves += 1
            self.object.move(5, 0)
            
w = g.GraphWin("Window", 500, 500)
w.setBackground("white")
p = Player(w, 250, 250)
key = "z"
while key != "q":
    key = w.checkKey()
    p.control(key)
w.close()