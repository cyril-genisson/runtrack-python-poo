#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job09.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""

class Produit:
    def __init__(self, nom, prix, tva):
        self.nom = nom
        self.prixHT = prix
        self.tva = tva

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        return self.nom, self.prixHT, self.tva

    def change_nom(self, nom):
        self.nom = nom

    def affiche_nom(self):
        return self.nom

    def change_prix(self, prix):
        self.prixHT = prix

    def affiche_prix(self):
        return self.prix

    def change_tva(self, tva):
        self.tva = tva

    def affiche_tva(self):
        return self.tva


if __name__ == "__main__":
    prod1 = Produit("Pain au chocolat", 0.8, 5.5)
    nom, prixHT, tva = prod1.afficher()
    prixTTC = prod1.CalculerPrixTTC()   
    print(f"Nom du produit: {nom}")
    print(f"Prix HT du produit: {prixHT}€")
    print(f"TVA du produit: {tva}%")
    print(f"Prix TTC du produit: {prixTTC}€\n")

    prod1.change_nom("Croissant")
    prod1.change_prix(0.5)
    prod1.change_tva(20)
    nom, prixHT, tva = prod1.afficher()
    prixTTC = prod1.CalculerPrixTTC()   
    print(f"Nom du produit: {nom}")
    print(f"Prix HT du produit: {prixHT}€")
    print(f"TVA du produit: {tva}%")
    print(f"Prix TTC du produit: {prixTTC}€\n")

