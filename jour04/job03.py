#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job03.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""


class Rectangle:
    def __init__(self, width, length):
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

    def perimetre(self):
        return 2 * (self.get_width() + self.get_length())

    def surface(self):
        return self.get_width() * self.get_length()


class Parallelepipede(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width=width, length=length)
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def volume(self):
        return self.surface() * self.__height


if __name__ == "__main__":
    rec = Rectangle(3, 10)
    print(f"Dimensions du rectangle: Longueur: {rec.get_length()}   Largeur: {rec.get_width()}")
    print(f"Périmère: {rec.perimetre()}  Aire: {rec.surface()}")

    para= Parallelepipede(3, 10, 7)
    print(f"Dimensions du parallélépipède: Longueur: {para.get_length()}  Largeur: {para.get_width()}  Hauteur: {para.get_height()}")
    print(f"Volume: {para.volume()}")

