#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job03.py
@created: 04/01/2024

@project: 
@licence: GPLv3
"""
import itertools


class Tache:
    def __init__(self, title, description, status):
        self.__title = title
        self.__description = description
        self.__status = status

    def get_id(self):
        return self.__id_task

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


class ListeDeTaches:
    with open("id_task.txt", "r") as f:
        l = int(f.readline()) + 1
        id_task = itertools.count(l)

    def __init__(self):
        self.__task = []

    def ajouterTache(self, title, description, status):
        self.__id_task = next(ListeDeTaches.id_task)
        with open("id_task.txt", "w") as f:
            f.write(str(self.__id_task))
        self.__task.append({'id_task': self.__id_task, 'task': Tache(title, description, status)})

    def supprimerTache(self, id_task):
        for k in range(len(self.__task)):
            if self.__task[k]['id_task'] == id_task:
                self.__task.pop(k)
                break

    def marquerCommeFinie(self, id_task):
        for k in range(len(self.__task)):
            if self.__task[k]['id_task'] == id_task:
                self.__task[k]['task'].set_status('Terminée')
                break

    def afficherListe(self):
        Id, Titre, Description, Status = "Id", "Titre", "Description", "Status"
        print(f"{Id:^5}|{Titre:^30}|{Description:^60}|{Status:^15}")
        print(f"{'-' * 113}")
        for k in range(len(self.__task)):
            print(f"{self.__task[k]['id_task']:<5}|{self.__task[k]['task'].get_title():^30}|{self.__task[k]['task'].get_description():^60}|{self.__task[k]['task'].get_status():^15}")

    def filterListe(self, status):
        Id, Titre, Description, Status = "Id", "Titre", "Description", "Status"
        print(f"{Id:^5}|{Titre:^30}|{Description:^60}|{Status:^15}")
        print(f"{'-' * 113}")
        for k in range(len(self.__task)):
            if self.__task[k]['task'].get_status() == status:
                print(f"{self.__task[k]['id_task']:<5}|{self.__task[k]['task'].get_title():^30}|{self.__task[k]['task'].get_description():^60}|{self.__task[k]['task'].get_status():^15}")
        

if __name__ == "__main__":
    from random import randint

    taches = ListeDeTaches()
    var, last = 10, 0
    for k in range(1, var + 1):
        title, description, status = f"Titre {k}", f"Description de la tâche {k}", "En cours"
        taches.ajouterTache(title, description, status)
    taches.afficherListe()
    with open("id_task.txt", "r") as f:
        last = int(f.readline())


    taches.marquerCommeFinie(randint(last - var, last))
    taches.marquerCommeFinie(randint(last - var, last))
    print("\n\n")
    taches.filterListe("Terminée")
    print("\n\n")
    taches.filterListe("En cours")

