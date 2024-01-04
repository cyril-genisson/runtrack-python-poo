#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job01.py
@created: 04/01/2024

@project: 
@licence: GPLv3
"""

class Ville:
    def __init__(self, name, nb_residents):
        self.__name = name
        self.__nb_residents = nb_residents

    def get_name(self):
        return self.__name

    def get_nbresidents(self):
        return self.__nb_residents

    def add_residents(self, nb=1):
        self.__nb_residents += nb

    def rm_residents(self, nb=1):
        if self.__nb_residents >= nb:
            self.__nb_residents -= nb


class Personne:
    def __init__(self, name, age, town):
        self.__name = name
        self.__age = age
        self.__town = town
        self.ajouterPopulation()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self, age):
        return self.__age

    def get_town(self):
        return self.__town._Ville__name

    def ajouterPopulation(self):
        self.__town._Ville__nb_residents += 1


if __name__ == "__main__":
    ville75 = Ville("Paris", 1000000)
    ville13 = Ville("Marseille", 861635)

    print(f"ville: {ville75.get_name()}\t\t nb d'habitants: {ville75.get_nbresidents()}")
    print(f"ville: {ville13.get_name()}\t nb d'habitants: {ville13.get_nbresidents()}")

    pers1 = Personne("John", 45, ville75)
    pers2 = Personne("Myrtille", 4, ville75)
    pers3 = Personne("Chloé", 18, ville13)
    
    print(f"ville: {ville75.get_name()}\t\t nb d'habitants: {ville75.get_nbresidents()}")
    print(f"ville: {ville13.get_name()}\t nb d'habitants: {ville13.get_nbresidents()}")

