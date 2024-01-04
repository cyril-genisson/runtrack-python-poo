#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job03.py
@created: 03/01/2024

@project: 
@licence: GPLv3
"""

class Livre:
    def __init__(self, title, author, nb_pages):
        self.__title__ = title
        self.__author__ = author
        self.__nb_pages__ = nb_pages
        self.__disponible__ = True

    def get_title(self):
        return self.__title__
        
    def set_title(self, title):
        self.__title__ = title

    def get_author(self):
        return self.__author__
        
    def set_author(self, author):
        self.__author__ = author
            
    def get_pages(self):
        return self.__nb_pages__
        
    def set_pages(self, nb_pages):
        self.__nb_pages__ = nb_pages

    def get_disponibility(self):
        return self.__disponible__

    def emprunter(self):
        if self.get_disponibility():
            self.__disponible__ = False
        else:
            print("This book is not available.")

    def rendre(self):
        if self.get_disponibility() is False:
            self.__disponible__ = True

