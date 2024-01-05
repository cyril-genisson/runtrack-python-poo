#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job05.py
@created: 04/01/2024

@project: 
@licence: GPLv3
"""
from random import randint

class Personnage:
    def __init__(self, nom: str="", vie: int=100):
        self.__nom = nom
        self.__vie = vie
        self.__dead = False

    def get_name(self):
        return self.__nom

    def set_name(self, name):
        self.__nom = name

    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        self.__vie = vie

    def loose_life(self, pts):
        if self.__vie > pts:
            self.__vie -= pts
        else:
            self.__vie = 0
            self.__dead = True

    def get_alive(self):
        if not self.__dead:
            return True
        else:
            return False

    def attaquer(self, ennemy, pts):
        ennemy.loose_life(pts)


class Jeu:
    def __init__(self):
        self._level = "Easy"

    def choisirNiveau(self, level):
        print(f"Level: {level}")
        self._level = level

    def lancerJeu(self, name):
        match self._level:
            case 'Easy':
                player1 = Personnage(name, 100)
                player2 = Personnage("Ennemy", 60)
            case 'Medium':
                player1 = Personnage(name, 100)
                player2 = Personnage('Ennemy', 100)
            case 'Hard':
                player1 = Personnage(name, 60)
                player2 = Personnage('Ennemy', 100)
        
        print("Game start! Fight")
        runner = True
        print(f"{player1.get_name()} life {player1.get_vie()}")
        print(f"{player2.get_name()} life {player2.get_vie()}")
        while runner:
            if player1.get_alive() and player2.get_alive():
                pts = randint(1, 20)
                player1.attaquer(player2, pts)
                print(f"{player1.get_name()} attack {player2.get_name()}: damage {pts} pts")
            else:
                runner = False
            if player2.get_alive() and player2.get_alive():
                pts = randint(1, 20)
                player2.attaquer(player1, pts)
                print(f"{player2.get_name()} attack {player1.get_name()}: damage {pts} pts")
            else:
                runner = False
            print(f"{player1.get_name()} life {player1.get_vie()}")
            print(f"{player2.get_name()} life {player2.get_vie()}")

        if player1.get_alive() and not player2.get_alive():
            print(f"{player1.get_name()}: you win! END GAME")
        else:
            print(f"{player1.get_name()}: you loose! GAME OVER")


if __name__ == "__main__":
    game = Jeu()

    print("Choose difficulty")
    print("1: Easy\t2: Medium\t3: Hard")
    level = input("Enter your choice (1/2/3): ")
    match level:
        case '1':
            game.choisirNiveau("Easy")
        case '2':
            game.choisirNiveau("Medium")
        case '3':
            game.choisirNiveau("Hard")
        case _:
            print("Bad choice: enter un integer 1, 2 or 3")
            level = input("Enter your choice (1/2/3): ")
    name = input("Enter player name: ")
    game.lancerJeu(name)

