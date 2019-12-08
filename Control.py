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
        self.levelcount = levelcount
        
        
        self.w = g.GraphWin("Window", 600, 600)
        # bg must be a GIF
        background = g.Image((g.Point(300,300)), "corn_bg.gif")
        background.draw(self.w)
        self.maze = m.Maze(self.levelcount)
        self.draw_maze()
        self.play_maze()

    def draw_maze(self):
        scaling = self.w.getHeight()/self.maze.dimensions

        for row in range(self.maze.dimensions):
            for col in range(self.maze.dimensions):
                if self.maze.check_wall(row, col) == "empty":
                    path = g.Rectangle(g.Point(col * scaling, row * scaling), g.Point((col+1)*scaling, (row+1)*scaling))
                    path.setFill("yellow")
                    path.draw(self.w)
                    
        end_line = g.Rectangle(g.Point(self.maze.end[1]*scaling, self.maze.end[0]*scaling), g.Point((self.maze.end[1]+1)*scaling, (self.maze.end[0]+1)*scaling))
        end_line.setFill("red")
        end_line.draw(self.w)

        self.player = p.Player(self.w, self.maze.start[0]*scaling, self.maze.start[1]*scaling, self.maze, scaling)
        
    def play_maze(self):
        k = None
        while k!= "q":
            k=self.w.checkKey()
            self.player.control(k)
            
            cur_r, cur_c = self.player.get_location()
            
            if (cur_r == self.maze.end[0]) and (cur_c == self.maze.end[1]):
                
                break
           
        self.w.close()
        


levelcount = 0

while levelcount < 6:
    levelcount += 1
    L = Level(levelcount)
    print('Level', levelcount, 'finished!')
    if levelcount>6:
        break
    
            
            



    
    
