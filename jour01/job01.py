#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job01.py
@created: 02/01/2024

@project: 
@licence: GPLv3
"""

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

if __name__ == "__main__":
    op = Operation(12, 3)
    print(op)
