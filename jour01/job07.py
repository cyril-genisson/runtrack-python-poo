#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job07.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""

class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.velocity = 1

    def position(self):
        return self.x, self.y

    def gauche(self):
        self.x -= velocity
    
    def droite(self):
        self.x += velocity
    
    def bas(self):
        self.y -= velocity

    def haut(self):
        self.y += velocity
