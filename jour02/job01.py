#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job01.py
@created: 03/01/2024

@project: 
@licence: GPLv3
"""

class Rectangle:
    def __init__(self, longueur=1, largeur=1):
        self.__longueur__ = longueur
        self.__largeur__ = largeur

    def get_geometry(self):
        return self.__longueur__, self.__largeur__
    
    def set_geometry(self, longueur, largeur):
        self.__longueur__ = longueur
        self.__largeur__ = largeur

    def get_longueur(self):
        return self.__longueur__

    def set_longueur(self, longueur):
        self.__longueur__ = longueur
    
    def get_largeur(self):
        return self.__largeur__

    def set_largeur(self, largeur):
        self.__largeur__ = largeur


if __name__ == "__main__":
    rectangle = Rectangle(longueur=10, largeur=5)
    print(f"(L, l) = {rectangle.get_geometry()}")
    rectangle.set_longueur(30)
    print(f"(L, l) = {rectangle.get_geometry()}")

