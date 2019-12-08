import graphics as g
#import numpy as np
# Importing Isa's class to use
import maze_class as m
# import Control as c

class Player:
    def __init__(self, w, x, y, maze, scaling):
        self.w = w
        self.x = x + scaling//2 #to center
        self.y = y + scaling // 2
        self.maze = maze
        self.scaling = scaling
        self.draw()
        self.location = self.object.getCenter()
        self.r = int(self.location.getY() // self.scaling)
        self.c = int(self.location.getX() // self.scaling)
        
    # Making the visual representation of the player
    def draw(self):
        self.object = g.Circle(g.Point(self.x, self.y), self.scaling//4)
        self.object.setFill("DarkViolet")
        self.object.draw(self.w)
        
    # Allows for keyboard control and does not allow moves if wall is present
    def control(self, key):
        scaling = self.w.getHeight()/self.maze.dimensions
        self.key = key
        # counter for every player move made
        # scaling = 1200/m.Maze().get_name.dimensions
        # Allows for either arrows or WASD movement
        if key == "Up" and self.maze.check_wall(self.r-1, self.c) != "wall" and self.object.getCenter().getY() >= scaling or key == "w" and self.maze.check_wall(self.r-1, self.c) != "wall" and self.object.getCenter().getY() >= scaling:
            self.object.move(0, -self.scaling)
        # DOWN doesn't work properly for stopping at walls
        if (key == "Down" and self.maze.check_wall(self.r+1, self.c) != "wall") and self.object.getCenter() >= scaling or (key == "s" and self.maze.check_wall(self.r+1, self.c) != "wall"):
            self.object.move(0, self.scaling)
        if key == "Left" and self.maze.check_wall(self.r, self.c-1) != "wall" and self.object.getCenter().getX() >= scaling or key == "a" and self.maze.check_wall(self.r, self.c-1) != "wall" and self.object.getCenter().getX() >= scaling:
            self.object.move(-self.scaling, 0)
        # RIGHT doesn't work for the walls. LEFT and UP work
        if key == "Right" and self.maze.check_wall(self.r, self.c+1) != "wall" and self.object.getCenter().getX() >= self.maze.dimensions or key == "d" and self.maze.check_wall(self.r, self.c+1) != "wall":
            self.object.move(self.scaling, 0)
            
        self.location = self.object.getCenter()
        self.r = int(self.location.getY() // self.scaling)
        self.c = int(self.location.getX() // self.scaling)


    def get_location(self):
        return (self.r, self.c)
    
    def get_moves(self):
        return self.moves
            
# w = g.GraphWin("Window", 1200, 1200)
# # bg must be a GIF
# background = g.Image((g.Point(600,600)), "corn_bg.gif")
# background.draw(w)



# p = Player(w, 300, 300)
# key = "z"
# while key != "q":
    # key = w.checkKey()
    # p.control(key)
# w.close()
