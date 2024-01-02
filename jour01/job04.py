#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job04.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")


if __name__ == "__main__":
    pers01 = Personne(prenom="John", nom="Doe")
    pers02 = Personne(prenom="Jean", nom="Dupond")

    pers01.SePresenter()
    pers02.SePresenter()
