#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: constantes.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""
from enum import Enum

NB_PAQUETS = 5
BET_MINI = 5
BET_MAXI = 500
DEM_MONNAIE = 10000

class COULEUR(Enum):
    P = "Pique"
    C = "Coeur"
    D = "Carreau"
    T = "Trèfle"

class ACTION(Enum):
    HIT = 'h'
    STAND = 's'
    DOUBLE = 'd'
