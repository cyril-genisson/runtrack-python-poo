#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job05.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""
from job04 import Forme, Rectangle
from math import pi

class Cercle:
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def aire(self):
        return pi * self.get_radius() ** 2


if __name__ == "__main__":
    rec = Rectangle(3, 10)
    cercle = Cercle(10)
    print(f"Dimension du rectangle: Longueur: {rec.get_length()}  Largeur: {rec.get_width()}")
    print(f"Aire du rectangle: {rec.aire()}")
    print(f"Rayon du cercle: {cercle.get_radius()}")
    print(f"Aire du cercle: {cercle.aire()}")

