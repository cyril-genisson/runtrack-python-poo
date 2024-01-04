#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job02.py
@created: 04/01/2024

@project: 
@licence: GPLv3
"""

class CompteBancaire:
    def __init__(self, id_account, name, surname, balance, overdraft):
        self.__id_account = id_account
        self.__name = name
        self.__surname = surname
        self.__balance = balance
        self.__overdraft = overdraft
        self.__agios_rate = 0.05

    def get_id(self):
        return self.__id_account

    def get_balance(self):
        return self.__balance

    def afficher(self):
        print(f"Numéro de compte: {self.__id_account}")
        print(f"Titulaire: {self.__surname} {self.__name}")
        self.afficherSolde()

    def afficherSolde(self):
        print(f"Solde du compte n°{self.get_id()}: {self.__balance} €")

    def versement(self, payment):
        self.__balance += payment

    def retrait(self, withdrawal):
        if type(withdrawal) == int:
            if self.__balance >= withdrawal or self.__overdraft is True:
                self.__balance -= withdrawal
                self.afficherSolde()
                return True
            else:
                print(f"Solde insuffisant pour un retrait de {withdrawal}€ sur le compte n°{self.get_id()}")
                self.afficherSolde()
                return False

    def agios(self):
        if self.__balance < 0:
            self.__balance -= self.__balance * self.__agios_rate

    def virement(self, account, transfert_amount):
        if self.retrait(transfert_amount):
            account.versement(transfert_amount)


if __name__ == "__main__":
    compte1 = CompteBancaire(1, "Doe", "John", 10000, False)
    compte2 = CompteBancaire(2, "Dilan", "Bob", 2000, True)

    compte1.afficher()
    compte2.afficher()

    compte1.versement(2000)
    compte1.retrait(20000)
    compte2.retrait(5000)

    compte1.afficher()
    compte2.afficher()
    compte1.virement(compte2, abs(compte2.get_balance()))
    compte1.afficher()
    compte2.afficher()
