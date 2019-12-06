# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:24:18 2019

@author: isabe
"""
import numpy as np
import random
class Maze:
    def __init__(self,levelcount):
        self.level = levelcount
        self.dimensions = 5*self.level
        self.start = None
        self.end = None
        self.make_maze()
        self.generate_location()
        
    
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
        if self.maze[x,y] == 1:
            path = 'empty'
           
        elif self.maze[x,y] == 0:
            path = 'wall'
        return path             
    
    def generate_location(self):    
         start_location = (random.randint(0, self.dimensions-1),  random.randint(0, self.dimensions-1))
         while self.check_wall(start_location[0], start_location[1])== 'wall':
            start_location = (random.randint(0, self.dimensions-1),  random.randint(0, self.dimensions-1))
         finish = (random.randint(0, self.dimensions-1),  random.randint(0, self.dimensions-1))
         while self.check_wall(finish[0], finish[1])== 'wall':
            finish = (random.randint(0, self.dimensions-1),  random.randint(0, self.dimensions-1))
         self.start = start_location
         self.end = finish
             
