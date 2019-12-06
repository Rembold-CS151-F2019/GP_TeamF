# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:24:18 2019

@author: isabe
"""
import numpy as np
import random
class Maze:
    def __init__(self, level):
        self.level = level
        self.dimensions = 5*level
        self.make_maze()
        
    
    def get_name(self):
        dimensions = self.dimensions 
        return dimensions 
    
    
    def make_maze(self):
        self.maze= np.ones((self.dimensions, self.dimensions))
        for c in range(1,3*self.level):
            x = random.randint(0, self.dimensions-1)
            y = random.randint(0, self.dimensions-1)
            self.maze[x,y] = 0
        return self.maze
            
            
    def check_wall(self, x, y):
        if self.maze[x,y]== 1:
            path = 'empty'
           
        elif self.maze[x,y] == 0:
            path = 'wall'
        return path             
      
        