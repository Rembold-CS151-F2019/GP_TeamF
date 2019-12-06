import graphics as g
#import numpy as np
# Importing Isa's class to use
import maze_class as m


class Player:
    def __init__(self, w, x, y, maze, scaling):
        self.w = w
        self.x = x + scaling//2 #to center
        self.y = y + scaling // 2
        self.maze = maze
        self.scaling = scaling
        self.draw()
        self.location = self.object.getCenter()
        
    # Making the visual representation of the player
    def draw(self):
        self.object = g.Circle(g.Point(self.x, self.y), 20)
        self.object.setFill("DarkViolet")
        self.object.draw(self.w)
        
    # Allows for keyboard control and does not allow moves if wall is present
    def control(self, key):
        self.key = key
        # counter for every player move made
        moves = 0
        # scaling = 1200/m.Maze().get_name.dimensions
        # Allows for either arrows or WASD movement
        if key == "Up" and self.maze.check_wall(self.get_location, self.get_location - self.scaling) != "wall" or key == "w" and self.maze.check_wall(self.get_location, self.get_location - scaling) != "wall":
            moves += 1
            self.object.move(0, -20)
        if key == "Down" and self.maze.check_wall(self.get_location, self.get_location + self.scaling) != "wall" or key == "s" and self.maze.check_wall(self.get_location, self.get_location + self.scaling) != "wall":
            moves += 1
            self.object.move(0, 20)
        if key == "Left" and self.maze.check_wall(self.get_location - self.scaling, self.get_location) != "wall" or key == "a" and self.maze.check_wall(self.get_location - self.scaling, self.get_location) != "wall":
            moves += 1
            self.object.move(-20, 0)
        if key == "Right" and self.maze.check_wall(self.get_location + self.scaling, self.get_location) != "wall" or key == "d" and self.maze.check_wall(self.get_location + self.scaling, self.get_location) != "wall":
            moves += 1
            self.object.move(20, 0)
            
    def get_location(self):
        location = self.location
        return location
            
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
