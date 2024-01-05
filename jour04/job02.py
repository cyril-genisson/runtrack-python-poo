#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job02.py
@created: 05/01/2024

@project: 
@licence: GPLv3
"""
from job01 import Personne, Eleve, Professeur

if __name__ == "__main__":
    student = Eleve()
    student.bonjour()
    student.modifierAge(15)
    student.afficherAge()
    master = Professeur()
    master.modifierAge(40)
    master.afficherAge()
    master.enseigner()


