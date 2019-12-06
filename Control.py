#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:30:03 2019

@author: ambergriffith
"""

import graphics as g
import maze_class as m
import Player_class as p

class Level():
    def __init__(self, levelcount):
        self.levelcompleted = False
        self.levelcount = 1
        
        
        self.w = g.GraphWin("Window", 1200, 1200)
        # bg must be a GIF
        background = g.Image((g.Point(600,600)), "corn_bg.gif")
        background.draw(self.w)
        self.maze = m.Maze(self.levelcount)
        self.draw_maze()
        self.play_maze()

    def draw_maze(self):
        scaling = 1200/self.maze.dimensions

        for row in range(self.maze.dimensions):
            for col in range(self.maze.dimensions):
                if self.maze.check_wall(row, col) == "empty":
                    path = g.Rectangle(g.Point(col * scaling, row * scaling), g.Point((col+1)*scaling, (row+1)*scaling))
                    path.setFill("yellow")
                    path.draw(self.w)

        self.player = p.Player(self.w, self.maze.start[0]*scaling, self.maze.start[1]*scaling, self.maze, scaling)
        
    def play_maze(self):
        k = None
        while k!= "q" and self.levelcompleted ==False:
            k=self.w.checkKey()
            self.player.control(k)
            if self.player.get_location() == self.maze.end:
                self.levelcompleted == True
                self.lost = False
        self.lost = True
        

#w = g.GraphWin("Window", 1200, 1200)
 # bg must be a GIF
#background = g.Image((g.Point(600,600)), "corn_bg.gif")
#background.draw(w)
#scaling = 1200/m.Maze().get_name.dimensions
#player = p.Player(w, m.Maze.start[0], m.Maze.start[1])
#key = "z"
levelcount = 0
#while key != "q":
    #key = w.checkKey()
    #p.control(key)
while levelcount < 6:
    levelcount += 1
    L = Level(levelcount)
    if Level.self.levelcompleted == False:
        break
    
            
            



    
    
