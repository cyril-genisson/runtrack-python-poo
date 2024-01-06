#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: carte.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""
from constantes import *

class Carte:
    couleur_carac = {COULEUR.P: "\u2660",
                     COULEUR.H: "\u2665",
                     COULEUR.D: "\u2666",
                     COULEUR.T: "\u2663"}

    def __init__(self, couleur, valeur, facedown=False):
        self.__couleur = couleur
        self.__symbole = self.couleur_carac[couleur]
        self.__valeur = str(valeur)
        self.__facedown = facedown

    def get_couleur(self):
        return self.__symbole, self.__couleur

    def get_valeur(self):
        return self.__valeur

    def get_facedown(self):
        return self.__facedown
    
    def get_infos(self):
        return self.get_valeur(), self.get_couleur(), self.get_facedown()

    def retourne(self):
        self.__facedown = not self.__facedown


if __name__ == "__main__":
    pass

