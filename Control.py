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
    def __init__(self, level, window):
        self.level = 1
        self.w = window
        
    def level_up(self):
        self.level = 1
        w = g.GraphWin('Maze', 800, 800)
        w.setBackground('Green')
        
        k=""
        while k != "q":
            clickpoint =w.checkMouse()
            k=w.checkKey()
            
            player.control(k)
        
        w.close()
        
        if player.moves<= 10:
            self.level+=1
            return self.level
    
        w = g.GraphWin('Maze', 800, 800)
        w.setBackground('Green')
        
        k=""
        while k != "q":
            clickpoint =w.checkMouse()
            k=w.checkKey()
            
            player.control(k)
    
        w.close()
        
        if self.level > 5:
            return "You have escaped the final maze!"
    def draw(self):
        if self.level+1:
            self.maze.draw(w)
            w = g.GraphWin('Maze', 800,800)
            w.setBackground('Green')
            maze = m.Maze()
            player = p.Player(w,0,0)
            player.draw(w)
            k=""
            while k != "q":
                clickpoint =w.checkMouse() #Don't think we need this, no clicking
                k=w.checkKey()
                player.control(k)
    
            w.close()   
            
w = g.GraphWin("Window", 1200, 1200)
# bg must be a GIF
background = g.Image((g.Point(600,600)), "corn_bg.gif")
background.draw(w)
scaling = 1200/m.Maze.get_name.dimensions

for row in range(m.Maze.get_name.dimensions):
    for col in range(m.Maze.get_name.dimensions):
        if m.Maze.check_wall(row, col) == "empty":
            path = g.Rectangle(g.Point(col * scaling, row * scaling), g.Point((col+1)*scaling, (row+1)*scaling))
            path.setFill("yellow")
            path.draw(w)


player = p.Player(w, 300, 300)
key = "z"
while key != "q":
    key = w.checkKey()
    p.control(key)
w.close()
    
            
            
#w = g.GraphWin('Maze', 800,800)
#w.setBackground('Green')
#maze = m.Maze(5)
#player = p.Player(w,0,0)
#player.draw(w)
#k=""
#while k != "q":
    #clickpoint =w.checkMouse()
    #k=w.checkKey()
    #player.control(k)
    
#w.close()     
    


    
    