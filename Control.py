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
        
        
        w = g.GraphWin("Window", 1200, 1200)
        # bg must be a GIF
        background = g.Image((g.Point(600,600)), "corn_bg.gif")
        background.draw(w)
        scaling = 1200/m.Maze().get_name.dimensions
        player = p.Player(w, m.Maze.start[0], m.Maze.start[1])

        for row in range(m.Maze().get_name.dimensions):
            for col in range(m.Maze().get_name.dimensions):
                if m.Maze().check_wall(row, col) == "empty":
                    path = g.Rectangle(g.Point(col * scaling, row * scaling), g.Point((col+1)*scaling, (row+1)*scaling))
                    path.setFill("yellow")
                    path.draw(self.w)
        
    def level_up(self):
        maze = m.Maze()
        k = None
        while k!= "q" and self.levelcompleted ==False:
            k=w.checkKey()
            p.control(k)
            if p.Player.get_location() == maze.end:
                self.levelcompleted == True
        

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
    if L.lost:
        break
w.close()
    
            
            



    
    