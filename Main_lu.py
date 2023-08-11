# -*- coding:utf-8 -*-
from pkgbibliotheque.GestionBiblio import *
from pkgbibliotheque.GestionDocument import *
def afficher_menu(lenth):
    print('*'*lenth)
    print('*', end = '')
    print(f"{'Bienvenue à votre bibliothèque':^{lenth-2}}", end = '')
    print('*')
    print('*', end = '')
    print(f"{'Faites un choix':^{lenth-2}}", end = '')
    print('*')
    print('*' * lenth)
    liste_menu = ('1    Ajouter adhérent', '2    Supprimer adhérent', '3    Afficher tous les adhérents',
                  '4    Ajouter Document', '5    Supprimer Document', '6    Afficher tous les Documents',
                  '7    Ajouter Emprunts', "8    Retour d'un Emprunt", '9    Afficher tous les Emprunts',
                  'Q    Quitter')
    for x in liste_menu:
        print(f"{'*':<5}", end='')
        print(f"{x:<{lenth - 6}}", end='')
        print('*')
    print('*' * lenth)

lenth = 50
choix = ''

while choix != 'Q':
    afficher_menu(lenth)
    choix = input('Choisissez une action:').strip()
    if choix == '1':
        Biblio.ajouter_adherent()
    elif choix == '2':
        Biblio.supprimer_adherent()
    elif choix == '3':
        Biblio.lister_adherent()
    elif choix == '4':
        Biblio.ajouter_document()
    elif choix == '5':
        Biblio.supprimer_document()
    elif choix == '6':
        Biblio.lister_document()
    elif choix == '7':
        Biblio.ajouter_emprunt()
    elif choix == '8':
        Biblio.supprimer_emprunt()
    elif choix == '9':
        Biblio.lister_emprunt()
    else:
        choix = input('Choix erroné!  Re-entrez:')
