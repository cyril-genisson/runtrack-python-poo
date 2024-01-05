#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job01.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""


class Personne:
    def __init__(self, age=14):
        self._age = age

    def afficherAge(self):
        print(f"Age: {self._age}")

    def modifierAge(self, age):
        self.__age = age

    def bonjour(self):
        print("Hello")


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def afficherAge(self):
        print(f"J'ai {self._age} ans")

    def allerEnCours(self):
        print("Je vais en cours")


class Professeur(Personne):
    def __init__(self, subject="Informatique"):
        super().__init__()
        self.__matiereEnseignee = subject

    def enseigner(self):
        print("Le cours va commencer")


if __name__ == "__main__":
    people = Personne()
    student = Eleve()
    student.afficherAge()
