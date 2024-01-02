#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job06.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""

class Animal:
    def __init__(self, prenom="", age=0):
        self.prenom = prenom
        self.age = age

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom


if __name__ == "__main__":
    ani = Animal()
    print(f"L'âge de l'animal {ani.age} ans")
    ani.vieillir()
    print(f"L'âge de l'animal {ani.age} ans")

    ani.nommer("Luna")
    print(f"L'animal se nomme {ani.prenom}")
