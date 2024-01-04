#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job05.py
@created: 03/01/2024

@project: 
@licence: GPLv3
"""

class Voiture:
    def __init__(self, brand, model, year, mileage):
        self.__brand__ = brand
        self.__model__ = model
        self.__year__ = year
        self.__mileage__ = mileage
        self.__en_marche__ = False
        self.__reservoir__ = 50

    def get_brand(self):
        return self.__brand__

    def set_brand(self, brand):
        if type(brand) == str:
            self.__brand__ = brand

    def get_model(self):
        return self.__model__

    def set_model(self, model):
        if type(model) == str:
            self.__model__ = model

    def get_year(self):
        return self.__year__

    def set_year(self, year):
        if type(year) = int and year > 1800:
            self.__year__ = year

    def get_milage(self):
        return self.__mileage__

    def set_milage(self, mileage):
        if type(mileage) == int and mileage >= 0:
        self.__mileage__ = mileage

    def demarrer(self):
        if self.__en_marche__ is False and self.__verifier__plein__() > 5:
            self.__en_marche__ = True
    
    def arreter(self):
        if self.__en_marche__ is True:
            self.__en_marche__ = False

    def __verifier_plein__(self):
        return self.__reservoir__

