#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job05.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print("abscisse: {self.x}\tordonnée: {self.y}")

    def afficherX(self):
        print("x: {self.x}")
    
    def afficherY(self):
        print("y: {self.y}")

    def changerX(self, x):
        self.x = x
    
    def changerY(self, y):
        self.y = y

