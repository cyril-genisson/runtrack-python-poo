#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job04.py
@created: 03/01/2024

@project: 
@licence: GPLv3
"""

class Student:
    def __init__(self, name, surname, student_id):
        self.__name__ = name
        self.__surname__= surname
        self.__student_id__ = student_id
        self.__credits__ = 0
        self.__level__ = self.__studentEval__()

    def add_credits(self, new):
        if type(new) == int and new > 0:
            self.__credits__ += new
    
    def get_name(self):
        return self.__name__

    def get_surname(self):
        return self.__surname__

    def get_id(self):
        return self.__student_id__

    def get_credits(self):
        return self.__credits__

    def __studentEval__(self):
        value = self.get_credits()
        if value < 60:
            return "Insuffisant"
        elif value < 70:
            return "Passable"
        elif value < 80:
            return "Bien"
        elif value < 90:
            return "Très bien"
        else:
            return "Excellent"

    def studentInfo(self):
        infos = [f"Nom = {self.get_name()}",
                 f"Prénom = {self.get_surname()}",
                 f"id = {self.get_id()}",
                 f"Niveau = {self.__studentEval__()}"
                ]

        for _ in infos:
            print(_)


if __name__ == "__main__":
    stud1 = Student("Doe", "John", 145)
    for _ in range(3):
        stud1.add_credits(10)
    print(f"Le nombre de crédits de {stud1.get_surname()} {stud1.get_name()} est de {stud1.get_credits()} points")
    stud1.add_credits(40)
    stud1.studentInfo()
