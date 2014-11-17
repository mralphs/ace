# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 23:05:52 2014

This is the sprite factory

@author: younga25
"""

from PyQt4 import QtGui, QtCore
from sets import Set
import math
import os

class SpriteDepth:
    TOP = "0"    
    NEAR = "1"
    CENTER = "2"
    FAR = "3"
    BACK = "4"
    
class SpriteType:
    APHANOTHECE_OUTLINE = [0, 0, 0, 2, 3]
    APHANOTHECE_RENDER1 = [1]
    COUNT = 4
    
class BackgroundType:
    CYAN_SOLID = "0"
    GRAY_SOLID = "1"
    
class SpriteFactory:
    
    def __init__(self, directory):
        self.directory = directory
        self.sprite_paths = {}
        self.load_sprites()

    def load_sprites(self):
        for dirname, dirnames, filenames in os.walk( self.directory ):
            for filename in filenames:
                
                rotation = filename.split(".")[0][1:]
                if not rotation.isdigit():
                    break
                elif(self.sprite_paths.has_key(dirname)):
                    self.sprite_paths[dirname].add(int(rotation))
                else:
                    self.sprite_paths[dirname] = Set([int(rotation)])
 
               
    def get_sprite(self, code, depth, rotation):
        """Gets the sprite with the closest rotation and return the amount 
        require to rotate""" 
        dirname = os.path.join(self.directory,"t"+str(code),"d"+str(depth))
        filename = None
        diff = 360

        if dirname in self.sprite_paths:
            closest = -1
            rotation_rounded = ((int)(math.floor(rotation)/15)*15)
            filename = "r"+str(rotation_rounded)+".png"
            
            for degree in self.sprite_paths[dirname]:
                if degree == 0 and rotation > 180:
                    degree = 360
                test = (rotation - degree)
                if math.fabs(test) <= math.fabs(diff):
                    diff = test
                    closest = degree
            filename = "r"+str(closest%360)+".png"
            
        return os.path.join(dirname,filename), diff