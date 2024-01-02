#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job08.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""
from math import pi

class Cercle:
    def __init__(self, rayon):
        self.r = rayon

    def changerRayon(self, rayon):
        self.r = rayon

    def circonference(self):
        return 2 * pi * self.r

    def aire(self):
        return pi * self.r ** 2

    def diametre(self):
        return 2 * self.r

    def afficherinfos(self):
        print(f"Rayon du cercle: {self.r}")
        print(f"Diamètre du cercle: {self.diametre()}")
        print(f"Circonférence du cercle: {self.circonference()}")
        print(f"Aire du cercle: {self.aire()}")


if __name__ == "__main__":
    cercle1 = Cercle(4)
    cercle1.afficherinfos()

    cercle2 = Cercle(7)
    cercle2.afficherinfos()
