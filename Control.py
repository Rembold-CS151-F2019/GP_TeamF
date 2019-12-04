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
maze = m.Maze(5)
player = p.Player(w,0,0)
player.draw()
k=""
while k != "q":
    clickpoint =w.checkMouse()
    k=w.checkKey()
    player.control(k)
    
w.close()     
    


    
    
