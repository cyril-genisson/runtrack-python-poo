#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: dealer.py
@created: 06/01/2024

@project: 
@licence: GPLv3
"""
from constantes import *
from joueur import Joueur
from carte import Carte

class Dealer(Joueur):
    def __init__(self, nb_paquets=NB_PAQUETS):
        super().__init__("Dealer")
        self.sabot = []
        for _ in range(nb_paquets):
            self.init_sabot()
        self.pari = "0"
        self.money = 0
    
    def init_sabot(self):
        for k in list(range(2, 11)) + ['V', 'D', 'R', 'A']:
            for couleur in COULEUR:
                self.sabot.append(Carte(couleur, valeur))

    def deal(self, facedown=False):
        if len(self.sabot) == 0:
            return False
        carte = self.sabot.pop(randint(0, len(self.deck) - 1))
        if facedown:
            carte.retourne()
        return carte

    def revele(self):
        self.carte[1].retourne()

