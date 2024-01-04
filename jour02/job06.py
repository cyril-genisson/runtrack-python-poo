#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job06.py
@created: 03/01/2024

@project: 
@licence: GPLv3
"""
import itertools
import pandas as pd


class Commande:
    stat = {"C": "En cours", "T": "Terminée", "A": "Annulée"}
    with open("id.txt", "r") as f:
        l = int(f.readline()) + 1
        id_command = itertools.count(l)


    def __init__(self, status=stat["C"]):
        self.__id_command = next(Commande.id_command)
        with open("id.txt", "w") as f:
            f.write(str(self.get_id()))
        self.__table = {}
        self.__status = status
        self.__menu__ = pd.read_csv('menu.csv', index_col='id')
        self.__menu_dict__ = self.__menu__.set_index('article').T.to_dict('dict')

    def change_status(self, status):
        if status in stat and status != stat["C"]:
            self.__status = status[status]

    def get_id(self):
        return self.__id_command

    def get_status(self):
        return self.__status

    def set_status(self, status):
        if self.get_status() == self.stat['C'] and status.upper() != 'C':
            self.__status = self.stat[status.upper()]
            del self.__menu__
            del self.__menu_dict__

    def get_list(self):
        return self.__table

    def remove_course(self, course, quantity=1):
        if course in self.__menu_dict__ and self.get_status == self.stat['C']:
            if self.__table[course]['quantity'] - quantity > 0:
                self.__table[course]['quantity'] -= quantity
            else:
                del self.__table[course]

    def add_course(self, course, quantity=1):
        if course in self.__menu_dict__ and self.get_status() == self.stat['C']:
            self.__table[course] = self.__menu_dict__[course]
            self.__table[course]['quantity'] =  self.__table[course].get('quantity', 0) + quantity
    
    def __get_price(self):
        price = 0.
        for k in self.get_list():
            price += self.__table[k]['quantity'] * self.__table[k]['price_HT']
        return round(price, 2)

    def get_tva(self):
        price = 0.
        for k in self.get_list():
            price += self.__table[k]['quantity'] * self.__table[k]['price_HT'] * 0.01 * self.__table[k]['tva(%)']
        return round(price, 2)
        
    def get_bill(self):
        price = 0.
        for k in self.get_list():
            price += self.__table[k]['quantity'] * self.__table[k]['price_HT'] * ( 1 + 0.01 * self.__table[k]['tva(%)'])
        return round(price, 2)

    def resume_command(self):
        print(f"id command: {self.get_id()}")
        for k in self.get_list():
            print(f"{k}: {self.__table[k]['quantity']}")
        print(f"Bill: {self.get_bill()}€\tTVA: {self.get_tva()}€")

if __name__ == "__main__":
    from random import randint
    produit = ['Sushi', 'Burrito', 'Taco', 'Quesadilla', 'Pizza',
               'Pasta', 'Steak', 'Salad', 'Donut', 'Soda',
               'Beer', 'Wine', 'Water']
 
    var = 10
    commande = {}
    for k in range(var):
        commande[str(k)] = Commande()
        print(f"{'*' * 60}")
        commande[str(k)].resume_command()
        for _ in range(3):
            commande[str(k)].add_course(produit[randint(0, 12)], randint(1, 5))
        print(f"{'*' * 60}")
        commande[str(k)].resume_command() 
    commande[str(randint(0, var - 1))].set_status('A')
    commande[str(randint(0, var - 1))].set_status('T')

    print(f"{'*' * 60}")
    for k in range(len(commande)):
        print(f"id command: {commande[str(k)].get_id()}\t status: {commande[str(k)].get_status()}\t bill: {commande[str(k)].get_bill()}€") 

