#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job06.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""


class Vehicule:
    def __init__(self, brand, model, year, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, brand, model, year, price, doors=4):
        super().__init__(brand = brand, model=model, year=year, price=price)
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def set_doors(self, doors):
        self.__doors = doors

    def informationsVehicule(self):
        print(f"Marque = {self.get_brand()}")
        print(f"Modèle = {self.get_model()}")
        print(f"Année = {self.get_year()}")
        print(f"Prix = {self.get_price()}")
        print(f"Nombre de portes = {self.get_doors()}")

    def demarrer(self):
        print(f"Je roule avec {self.get_doors()} portes")


class Moto(Vehicule):
    def __init__(self, brand, model, year, price, wheels=2):
        super().__init__(brand = brand, model=model, year=year, price=price)
        self.__wheels = wheels

    def get_wheels(self):
        return self.__wheels

    def set_wheels(self, wheels):
        self.__wheels = wheels

    def informationsVehicule(self):
        print(f"Marque = {self.get_brand()}")
        print(f"Modèle = {self.get_model()}")
        print(f"Année = {self.get_year()}")
        print(f"Prix = {self.get_price()}")
        print(f"Nombre de roues = {self.get_wheels()}")

    def demarrer(self):
        print(f"Je roule avec {self.get_wheels()} roues")


if __name__ == "__main__":
    voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500)
    moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
    voiture1.informationsVehicule()
    voiture1.demarrer()
    print()
    moto1.informationsVehicule()
    moto1.demarrer()
