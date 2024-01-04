#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job02.py
@created: 03/01/2024

@project: 
@licence: GPLv3
"""

class Livre:
    def __init__(self, title, author, nb_pages):
        self.__title__ = title
        self.__author__ = author
        self.__nb_pages__ = nb_pages

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

