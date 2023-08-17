# -*- coding:utf-8 -*-
from pkgbibliotheque.GestionBiblio_lu import *
from pkgbibliotheque.GestionPersonne_lu import *
from pkgbibliotheque.GestionDocument_lu import *
import csv

def afficher_menu(lenth):
    print('*'*lenth)
    print('*', end = '')
    print(f"{'Bienvenue à votre bibliothèque':^{lenth-2}}", end = '')
    print('*')
    print('*', end = '')
    print(f"{'Faites un choix':^{lenth-2}}", end = '')
    print('*')
    print('*' * lenth)
    liste_menu = ['1    Ajouter adhérent', '2    Supprimer adhérent', '3    Afficher tous les adhérents',
                  '4    Ajouter Document', '5    Supprimer Document', '6    Afficher tous les Documents',
                  '7    Ajouter Emprunts', "8    Retour d'un Emprunt", '9    Afficher tous les Emprunts',
                  'Q    Quitter']
    for x in liste_menu:
        print(f"{'*':<5}", end='')
        print(f"{x:<{lenth - 6}}", end='')
        print('*')
    print('*' * lenth)

def lire_Adherents(fich):
    liste_Adherents = []
    with open(fich,'r') as fich:
        reader = csv.reader(fich, delimiter='\t')
        for ligne in reader:
            nom = ligne[0]
            prenom = ligne[1]
            age = ligne[2]
            num = ligne[3]
            liste_Adherents.append(Adherent(Personne(nom, prenom, age), num))
    return liste_Adherents

lenth = 50
choix = ''
myBiblio = Biblio()
myBiblio.liste_adherent = lire_Adherents('Adherents.cvs')

while choix != 'Q':
    afficher_menu(lenth)
    choix = input('Choisissez une action:').strip()
    if choix == '1':
        myBiblio.ajouter_adherent()
    elif choix == '2':
        nom = input("Nom:").strip()
        prenom = input("Prenom:").strip()
        trouve = False
        for x in myBiblio.liste_adherent:
            if x.nom == nom and x.prenom == prenom:
                myBiblio.supprimer_adherent(x)
                trouve = True
                print(x)
                print("Déjà supprimé!")
                anykey = input()
        if trouve == False:
            print("Ne trouve pas l'adherent!")

    elif choix == '3':
        myBiblio.lister_adherent()
        anykey = input()
    elif choix == '4':
        myBiblio.ajouter_document()
    elif choix == '5':
        myBiblio.supprimer_document()
    elif choix == '6':
        myBiblio.lister_document()
        anykey = input()
    elif choix == '7':
        myBiblio.ajouter_emprunt()
    elif choix == '8':
        myBiblio.supprimer_emprunt()
    elif choix == '9':
        myBiblio.lister_emprunt()
        anykey = input()
    else:
        choix = input('Choix erroné!  Re-entrez:')
