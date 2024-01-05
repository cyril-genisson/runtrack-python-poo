#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job04.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""

class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle:
    def __init__(self, width, length):
        super().__init__()
        self.__width = width
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def aire(self):
        return self.get_length() * self.get_width()


if __name__ == "__main__":
    rec = Rectangle(3, 10)
    print(f"Dimension du rectangle: Longueur: {rec.get_length()}  Largeur: {rec.get_width()}")
    print(f"Aire du rectangle: {rec.aire()}")
